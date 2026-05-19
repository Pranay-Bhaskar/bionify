# tests/test_extension.py
from fovea import fovea_ext

def test_extension_formats_text():
    out = fovea_ext.format_bionic_text("hello world", 0.5)
    assert "\033[1m" in out
    assert "\033[22m" in out