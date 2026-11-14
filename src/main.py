"""First Pico entry point; the USB serial console is the initial display."""

from iching import cast, draw


def main():
    print("I Ching calculator")
    print("Sample three-coin reading (top line first):")
    print(draw(cast()))


if __name__ == "__main__":
    main()
