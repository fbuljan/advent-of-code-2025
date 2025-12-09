from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    points = []
    
    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                x, y = (int(part) for part in line.split(','))
            except ValueError:
                continue
            points.append((x, y))

    largest_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            (x1, y1), (x2, y2) = points[i], points[j]
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            if area > largest_area:
                largest_area = area
    
    print(largest_area)

            

if __name__ == "__main__":
    main()
