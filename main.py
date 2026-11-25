"""Entry for The Dog Ate My Homework: writes the dog's excuse to /output/entry.txt."""

import os

TEXT = "Your honor, the homework smelled of bacon, offered me no treats, and the essay was titled 'Self-Control.' I did the class a favor."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
