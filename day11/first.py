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

    def dfs(node: str) -> int:
        if node == "out":
            return 1
        if node in memo:
            return memo[node]

        total = 0
        for nei in graph[node]:
            total += dfs(nei)

        memo[node] = total
        return total

    result = dfs("you")
    print(result)

if __name__ == "__main__":
    main()
