PYTHON ?= python3
VENV ?= .venv
MPREMOTE ?= $(VENV)/bin/mpremote
PORT ?= auto
BOOTSEL_MOUNT ?= /Volumes/RPI-RP2

.PHONY: help setup flash upload repl reset demo check

help:
	@printf '%s\n' \
	  'make setup             Install mpremote in a local virtual environment' \
	  'make flash UF2=...     Install MicroPython (Pico in BOOTSEL mode)' \
	  'make upload            Copy the app to the Pico and reset it' \
	  'make repl              Open the MicroPython REPL' \
	  'make reset             Reset the connected Pico' \
	  'make demo              Run a sample reading on this computer' \
	  'make check             Run the host-side tests' \
	  'Overrides: PORT=/dev/..., BOOTSEL_MOUNT=/path/to/RPI-RP2'

$(MPREMOTE):
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install mpremote

setup: $(MPREMOTE)

flash:
	@test -n "$(UF2)" || { echo 'Set UF2 to a downloaded Pico MicroPython .uf2 file'; exit 1; }
	@test -f "$(UF2)" || { echo 'UF2 file not found: $(UF2)'; exit 1; }
	@test -d "$(BOOTSEL_MOUNT)" || { echo 'BOOTSEL drive not found: $(BOOTSEL_MOUNT)'; exit 1; }
	cp "$(UF2)" "$(BOOTSEL_MOUNT)/"

upload: $(MPREMOTE)
	$(MPREMOTE) connect $(PORT) fs cp iching.py main.py : + reset

repl: $(MPREMOTE)
	$(MPREMOTE) connect $(PORT) soft-reset repl

reset: $(MPREMOTE)
	$(MPREMOTE) connect $(PORT) reset

demo:
	$(PYTHON) main.py

check:
	$(PYTHON) -m unittest discover -s tests
