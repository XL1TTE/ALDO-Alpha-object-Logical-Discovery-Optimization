import sys

from src.cli import interactive

def main() -> None:
    try:
        interactive.run()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Bye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
