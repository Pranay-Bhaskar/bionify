import sys
import logging
import bionify

bionify.set_prescription(0.6)
bionify.set_style(bold=True, color="magenta")

print("Running test sequence. You should see bold text formatting below...")

# Test Sequence 1: Logging stream interception via proxy
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SystemTest")
logger.info("Initializing socket connection to https://github.com/api/v1")
logger.error("Failed to parse configuration file at C:\\nginx\\nginx.conf")

print("\n--- EXPECTED ERROR TRACEBACK DEMONSTRATION BELOW ---")
print("The script is going to intentionally crash now to show you how tracebacks are formatted.\n")

# Test Sequence 2: Unhandled exception traceback interception
def faulty_orchestrator():
    # This will raise a terminal exception and route through bionic_excepthook
    raise ValueError("Unexpected JSON payload token received during parsing.")

faulty_orchestrator()