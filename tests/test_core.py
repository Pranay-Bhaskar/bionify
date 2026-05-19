# tests/test_core.py
import fovea

def test_prescription_clamps_low():
    fovea.set_prescription(0.0)
    assert fovea.get_intensity() == 0.1

def test_prescription_clamps_high():
    fovea.set_prescription(2.0)
    assert fovea.get_intensity() == 1.0