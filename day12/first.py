from pathlib import Path

def parse_input(text: str) -> tuple[list[list[str]], list[tuple[int, int, list[int]]]]:
    lines = [ln.rstrip("\n") for ln in text.splitlines()]
    i = 0

    shapes_raw: list[list[str]] = []
    while i < len(lines):
        ln = lines[i].strip()
        if not ln:
            i += 1
            continue
        if "x" in ln and ":" in ln:
            break
        if ln.endswith(":") and ln[:-1].isdigit():
            i += 1
            block = []
            while i < len(lines) and lines[i].strip() != "":
                block.append(lines[i].strip())
                i += 1
            shapes_raw.append(block)
        i += 1

    regions: list[tuple[int, int, list[int]]] = []
    while i < len(lines):
        ln = lines[i].strip()
        i += 1
        if not ln:
            continue
        left, right = ln.split(":", 1)
        w_s, h_s = left.strip().split("x")
        W, H = int(w_s), int(h_s)
        counts = [int(x) for x in right.strip().split()] if right.strip() else []
        regions.append((W, H, counts))

    return shapes_raw, regions


def count_dots(pattern):
    c = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == "#":
                c += 1
    return c

def main() -> None:
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    text = p.read_text(encoding="utf-8")
    shapes, regions = parse_input(text)

    counts = [count_dots(shape) for shape in shapes]

    sol = 0
    for (n, m, targets) in regions:
        c = 0
        for i in range(len(targets)):
            c += counts[i] * targets[i]
        if n * m > c:
            sol += 1

    print(sol)


if __name__ == "__main__":
    main()
