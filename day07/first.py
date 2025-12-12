from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    s_positions = []
    result = 0
    
    with p.open() as f:
        for line in f:
            line_array = []
            for index, char in enumerate(line.strip()):
                if char == 'S':
                    s_positions.append(index)
                line_array.append(char)

            new_s_positions = []
            for pos in set(s_positions):
                if line_array[pos] == '^':
                    new_s_positions.append(pos - 1)
                    new_s_positions.append(pos + 1)
                    result += 1
                else:
                    new_s_positions.append(pos)
            s_positions = new_s_positions
    
    print(result)

            

if __name__ == "__main__":
    main()
