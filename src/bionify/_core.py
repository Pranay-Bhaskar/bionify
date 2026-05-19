import os

COLORS = {
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "white": "\033[97m",
}

_intensity = float(os.getenv("BIONIFY_INTENSITY", "0.5"))
_prefix = "\033[1;96m"
_suffix = "\033[0m"

def set_prescription(intensity: float):
    global _intensity
    _intensity = max(0.1, min(1.0, float(intensity)))

def get_intensity() -> float:
    return _intensity

def set_style(bold: bool = True, color: str = "cyan"):
    global _prefix, _suffix
    color_code = COLORS.get(color.lower(), "")
    bold_code = "\033[1m" if bold else ""

    if bold and color_code:
        _prefix = f"{bold_code}{color_code}"
        _suffix = "\033[0m"
    elif bold:
        _prefix = bold_code
        _suffix = "\033[22m"
    elif color_code:
        _prefix = color_code
        _suffix = "\033[39m"
    else:
        _prefix = ""
        _suffix = ""

def set_color_ansi(prefix: str, suffix: str = "\033[0m"):
    global _prefix, _suffix
    _prefix = prefix
    _suffix = suffix

def get_ansi_tags():
    return _prefix, _suffix