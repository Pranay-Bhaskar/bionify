from colorama import just_fix_windows_console

just_fix_windows_console()

from ._core import set_prescription, set_style
from .hook import install_hooks

install_hooks()

__all__ = ["set_prescription", "set_style"]