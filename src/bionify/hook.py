import sys
import traceback
import logging
from typing import TextIO, Any

from . import bionify_ext
from ._core import get_intensity, get_ansi_tags

_original_excepthook = sys.excepthook

def _format_text(data: str) -> str:
    prefix, suffix = get_ansi_tags()
    return bionify_ext.format_bionic_text(data, get_intensity(), prefix, suffix)

class BionicFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        return _format_text(msg)

def bionic_excepthook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    styled_traceback = ""
    for line in tb_lines:
        if "site-packages" in line or "lib\\python" in line.lower() or "lib/python" in line.lower():
            styled_traceback += line
        else:
            styled_traceback += _format_text(line)

    original_stderr = getattr(sys.stderr, "_original_stream", sys.stderr)
    original_stderr.write(styled_traceback)
    original_stderr.flush()

class BionicStreamWrapper:
    def __init__(self, original_stream: TextIO):
        self._original_stream = original_stream

    def write(self, data: str):
        if not data:
            return 0
        return self._original_stream.write(_format_text(data))

    def flush(self):
        self._original_stream.flush()

    def __getattr__(self, name: str) -> Any:
        return getattr(self._original_stream, name)

def install_hooks():
    sys.excepthook = bionic_excepthook
    if not isinstance(sys.stderr, BionicStreamWrapper):
        sys.stderr = BionicStreamWrapper(sys.stderr)