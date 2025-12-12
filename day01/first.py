from pathlib import Path

def main():
    path = Path(__file__).parent / "first.txt"
    try:
        with path.open("r", encoding="utf-8") as f:
            rows = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    
    curr = 50
    zeroCount = 0
    for row in rows:
        first_char, rest = row[0], int(row[1:])
        num = rest % 100
        if first_char == "L":
            curr -= num
        elif first_char == "R":
            curr += num

        if curr == 0 or curr == 100:
            zeroCount += 1
        elif curr < 0:
            curr += 100
        elif curr > 99:
            curr -= 100

    print(zeroCount)
if __name__ == "__main__":
    main()