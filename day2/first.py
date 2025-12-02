from pathlib import Path

def main():
    p = Path('input.txt')
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    ranges = []  # list of (start, end) tuples

    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            for part in line.split(','):
                part = part.strip()
                if not part:
                    continue
                a, b = part.split('-', 1)
                start = int(a.strip())
                end = int(b.strip())
                ranges.append((start, end))

    res = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if isNumInvalidId(n):
                res += n

    print(res)

def isNumInvalidId(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


if __name__ == "__main__":
    main()