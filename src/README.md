# I Ching calculator firmware

MicroPython starter for the RP2040 Raspberry Pi Pico in `../hw`. The current
program generates one sample three-coin reading on boot and prints its six
lines over USB serial. Lines are stored bottom first; `*` marks a changing
line. The key matrix, OLED, hexagram lookup data, and the calculator's final
behavior are still to be implemented as the hardware design settles.

## Get started

1. Install `python3` and run `make setup` to create a local environment with
   `mpremote`.
2. Download the Pico (RP2040) MicroPython `.uf2` from the
   [official Pico page](https://micropython.org/download/RPI_PICO/).
3. Hold **BOOTSEL** while connecting the Pico by USB. Run
   `make flash UF2=/path/to/firmware.uf2`. On Linux, set
   `BOOTSEL_MOUNT=/path/to/RPI-RP2` as well.
4. Once the Pico restarts, run `make upload`, then `make repl` to restart it
   and see the reading. Press Ctrl-D in the REPL to draw another reading;
   press Ctrl-] to leave the REPL.

`make demo` runs the same entry point on your computer, and `make check` runs
the core tests. If more than one serial device is connected, set
`PORT=/dev/your-port` for `upload`, `repl`, or `reset`.

`make upload` replaces `main.py` and `iching.py` on the connected Pico.
