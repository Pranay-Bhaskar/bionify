import sys
import fovea

fovea.set_prescription(0.6)
sys.stderr.write("This is a direct stderr formatting test.\n")
raise RuntimeError("Fovea traceback test")