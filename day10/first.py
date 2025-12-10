import re
from pathlib import Path
from collections import deque

def min_presses(goal_state: int, button_masks: list[int], num_lights: int) -> int | None:
    start = 0
    if goal_state == start:
        return 0

    visited = {start}
    q = deque()
    q.append((start, 0))

    while q:
        state, dist = q.popleft()

        for mask in button_masks:
            next_state = state ^ mask
            if next_state == goal_state:
                return dist + 1
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, dist + 1))

    return None

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return
    
    result = 0
    
    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            pattern = re.search(r"\[(.*?)\]", line).group(1)
            raw_buttons = re.findall(r"\(([^()]*)\)", line)
            buttons = [
                [int(x) for x in part.split(",") if x.strip()]
                for part in raw_buttons
            ]
            goal_bits = ''
            for char in pattern:
                if char == ".":
                    goal_bits += '0'
                elif char == "#":
                    goal_bits += '1'
                else:
                    print(f"Invalid character in pattern: {char}")
                    return
                
            goal_state = int(goal_bits, 2)
            num_lights = len(pattern)

            button_masks = []
            for btn in buttons:
                mask = 0
                for idx in btn:
                    bit = num_lights - 1 - idx
                    mask |= 1 << bit
                button_masks.append(mask)

            presses = min_presses(goal_state, button_masks, num_lights)
            if presses is None:
                continue

            result += presses
    
    print(result)

if __name__ == "__main__":
    main()
