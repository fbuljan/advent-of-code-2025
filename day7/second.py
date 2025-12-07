from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    worlds = []
    first = True
    
    with p.open() as f:
        for line in f:
            if first:
                for char in line.strip():
                    worlds.append(0)
                    if char == 'S':
                        worlds[-1] = 1
                first = False
                continue
            for index, char in enumerate(line.strip()):
                if char == '^':
                    if worlds[index] > 0:
                        worlds[index - 1] += worlds[index]
                        worlds[index + 1] += worlds[index]
                        worlds[index] = 0
    
    result = sum(worlds)
    print(result)

            

if __name__ == "__main__":
    main()
