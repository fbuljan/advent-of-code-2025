from pathlib import Path
from collections import defaultdict

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    graph = defaultdict(list)

    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            left, right = line.split(":", 1)
            src = left.strip()
            dests = right.strip().split() if right.strip() else []

            graph[src].extend(dests)

            for d in dests:
                if d not in graph:
                    graph[d] = []

    memo = {}

    def dfs(node: str, cond1, cond2) -> int:
        if node == "dac":
            cond1 = True
        if node == "fft":
            cond2 = True
        if node == "out":
            if cond1 and cond2:
                return 1
            else:
                return 0
        if (node, cond1, cond2) in memo:
            return memo[(node, cond1, cond2)]

        total = 0
        for nei in graph[node]:
            total += dfs(nei, cond1, cond2)

        memo[(node, cond1, cond2)] = total
        return total

    result = dfs("svr", False, False)
    print(result)

if __name__ == "__main__":
    main()
