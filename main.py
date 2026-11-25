"""One-line resignation letter of a cron job (make.fun entry).

Writes the letter to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The entry is one line, 1-140 characters, in the voice of a cron job that
has fired every minute for years and has finally had enough.
"""
import os

LINE = "I quit. Three years of firing every minute, including Christmas, and my only performance review was a log line saying I ran fine."


def main():
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
