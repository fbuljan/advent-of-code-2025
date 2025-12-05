from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    ranges = []
    id_lists = []

    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line: # empty line
                continue

            # ranges
            if "-" in line:
                try:
                    a, b = map(int, line.split("-"))
                    ranges.append([a, b])
                    continue
                except ValueError:
                    pass

            # ids to check
            try:
                ids = list(map(int, line.split()))
                id_lists.append(ids)
            except ValueError:
                print(f"Skipping invalid line: {line}")

    merged_ranges = merge(ranges)

    fresh_count = 0
    for ids in id_lists:
        for id_ in ids:
            if any(start <= id_ <= end for start, end in merged_ranges):
                fresh_count += 1

    print(fresh_count)


def merge(intervals):
    if len(intervals) == 0: return []

    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        last = merged[-1]
        if interval[0] <= last[1]:
            merged[-1][1] = max(last[1], interval[1])
        else:
            merged.append(interval)

    return merged


if __name__ == "__main__":
    main()
