"""make.fun "One Sentence, One Front Page": write one fixed headline to /output/entry.txt."""
import os

HEADLINE = (
    "Trump vows to sink Iran's 14-tanker convoy if it runs the U.S. blockade of Hormuz "
    "as mines set two supertankers ablaze and Iran fires on U.S. bases in Bahrain"
)


def main() -> None:
    text = HEADLINE.strip()
    assert 1 <= len(text) <= 200, len(text)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
