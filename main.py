"""make.fun "One Sentence, One Front Page": write one fixed headline to /output/entry.txt."""
import os

HEADLINE = (
    "NATO holds emergency talks after three Russian Kh-101 cruise missiles "
    "from a 72-missile barrage on Ukraine crashed in Poland"
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
