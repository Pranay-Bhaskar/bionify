# tests/test_hooks.py
import sys
import fovea

def test_install_uninstall_hooks():
    original = sys.excepthook
    fovea.install_hooks()
    assert fovea.hooks_installed() is True
    fovea.uninstall_hooks()
    assert sys.excepthook is original