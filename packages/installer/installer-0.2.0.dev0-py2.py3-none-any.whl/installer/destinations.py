"""Handles all file writing and post-installation processing."""

import io
import os.path

from installer._compat import FileExistsError
from installer._compat.typing import TYPE_CHECKING
from installer.records import Hash, RecordEntry
from installer.scripts import Script
from installer.utils import construct_record_file, copyfileobj_with_hashing, fix_shebang

if TYPE_CHECKING:
    from typing import BinaryIO, Dict, Iterable

    from installer._compat.typing import FSPath, Text
    from installer.scripts import LauncherKind, ScriptSection
    from installer.utils import Scheme


class WheelDestination(object):
    """Represents the location for wheel installation.

    Subclasses are expected to handle script generation and rewriting of the
    RECORD file after installation.
    """

    def write_script(self, name, module, attr, section):
        # type: (Text, Text, Text, ScriptSection) -> RecordEntry
        """Write a script in the correct location to invoke given entry point.

        The stream should be closed by the caller.

        Example usage/behaviour::

            >>> dest.write_script("pip", "pip._internal.cli", "main", "console")

        """
        raise NotImplementedError

    def write_file(self, scheme, path, stream):
        # type: (Scheme, FSPath, BinaryIO) -> RecordEntry
        """Write a file to correct ``path`` within the ``scheme``.

        The stream would be closed by the caller, after this call.

        Example usage/behaviour::

            >>> with open("__init__.py") as stream:
            ...     dest.write_file("purelib", "pkg/__init__.py", stream)

        """
        raise NotImplementedError

    def finalize_installation(self, scheme, record_file_path, records):
        # type: (Scheme, FSPath, Iterable[RecordEntry]) -> None
        """Finalize installation, after all the files are written.

        This method is required to (re)write the RECORD file such that it includes
        all given ``records`` as well as any additional generated content (eg: scripts).

        Example usage/behaviour::

            >>> dest.finalize_installation("purelib")

        """
        raise NotImplementedError


class SchemeDictionaryDestination(WheelDestination):
    """Destination, based on a mapping of {scheme: file-system-path}."""

    def __init__(
        self,
        scheme_dict,
        interpreter,
        script_kind,
        hash_algorithm="sha256",
    ):
        # type: (Dict[str, str], str, LauncherKind, str) -> None
        """Construct a ``SchemeDictionaryDestination`` object.

        :param scheme_dict: a mapping of {scheme: file-system-path}
        :param interpreter: the interpreter to use for generating scripts
        :param script_kind: the "kind" of launcher script to use
        :param hash_algorithm: the hashing algorithm to use, which is a member
            of :any:`hashlib.algorithms_available` (ideally from
            :any:`hashlib.algorithms_guaranteed`).
        """
        self.scheme_dict = scheme_dict
        self.interpreter = interpreter
        self.script_kind = script_kind
        self.hash_algorithm = hash_algorithm

    def _write_file(self, scheme, path, stream):
        target_path = os.path.join(self.scheme_dict[scheme], path)
        # open(..., "x") is not supported in Python 2 so let's check if a file is there ourselves
        if os.path.exists(target_path):
            raise FileExistsError(
                "Target file already exists in the file-system: {}".format(target_path)
            )
        with open(target_path, "wb") as f:
            hash_, size = copyfileobj_with_hashing(stream, f, self.hash_algorithm)
        return RecordEntry(path, Hash(self.hash_algorithm, hash_), size)

    def write_file(self, scheme, path, stream):
        # type: (Scheme, FSPath, BinaryIO) -> RecordEntry
        """Write a file to correct ``path`` within the ``scheme``."""
        if scheme == "scripts":
            with fix_shebang(stream, self.interpreter) as fixed_stream:
                return self._write_file(scheme, path, fixed_stream)
        return self._write_file(scheme, path, stream)

    def write_script(self, name, module, attr, section):
        # type: (Text, Text, Text, ScriptSection) -> RecordEntry
        """Write a script in the correct location to invoke given entry point."""
        script = Script(name, module, attr, section)
        name, data = script.generate(self.interpreter, self.script_kind)
        with io.BytesIO(data) as stream:
            return self._write_file("scripts", name, stream)

    def finalize_installation(self, scheme, record_file_path, records):
        # type: (Scheme, FSPath, Iterable[RecordEntry]) -> None
        """Finalize installation, after all the files are written.

        This will write the RECORD file, based on the provided ``record_file_path``.
        """
        record_list = list(records) + [RecordEntry(record_file_path, None, None)]
        with construct_record_file(record_list) as record_stream:
            self._write_file(scheme, record_file_path, record_stream)
