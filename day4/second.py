from pathlib import Path

def main():
    p = Path('input.txt')
    if not p.exists():
        print(f"Input file not found: {p}")
        return
    
    matrix = []

    with p.open() as f:
        for line in f:
            row = []
            line = line.strip()
            for idx, ch in enumerate(line):
                if ch == '@':
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
    
    neighbours = []

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for i in range(rows):
        neigh_row = []
        for j in range(cols):
            count = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    count += matrix[ni][nj]
            neigh_row.append(count)
        neighbours.append(neigh_row)

    removed = 0

    # First iteration: check whole matrix
    to_check = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                to_check.add((i, j))

    while to_check:
        next_to_check = set()
        for i, j in to_check:
            if matrix[i][j] == 1 and neighbours[i][j] < 4:
                matrix[i][j] = 0
                removed += 1
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbours[ni][nj] -= 1
                        # Check neighbor in next iteration
                        if matrix[ni][nj] == 1:
                            next_to_check.add((ni, nj))
        to_check = next_to_check
    
    print(removed)

if __name__ == "__main__":
    main()