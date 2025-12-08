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
                x, y, z = (int(part) for part in line.split(','))
            except ValueError:
                continue
            points.append((x, y, z))

    distances = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = ((p1[0] - p2[0]) ** 2 + 
                    (p1[1] - p2[1]) ** 2 + 
                    (p1[2] - p2[2]) ** 2)
            distances.append((dist, i, j))
        
    distances.sort(key=lambda t: t[0])
    groups = []

    for dist, i, j in distances:
        gi = gj = None
        for g in groups:
            if i in g:
                gi = g
            if j in g:
                gj = g
            if gi is not None and gj is not None:
                break

        if gi is None and gj is None:
            groups.append({i, j})
        elif gi is not None and gj is None:
            gi.add(j)
        elif gi is None and gj is not None:
            gj.add(i)
        elif gi is not gj:
            gi.update(gj)
            groups.remove(gj)

        if len(groups) == 1 and len(groups[0]) == len(points):
            print(points[i][0] * points[j][0])
            break


if __name__ == "__main__":
    main()
