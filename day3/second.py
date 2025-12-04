import sys
from pathlib import Path

def main():
    p = Path('input.txt')
    if not p.exists():
        print(f"Input file not found: {p}")
        return
    
    sum = 0

    with p.open() as f:
        for line in f:
            line = line.strip()
            
            n = 12
            max_digits = []
            while n > 0:
                max_digit, max_ids = find_max_in_string(line[:len(line)-n+1])
                max_digits.append(max_digit)
                line = line[max_ids[0]+1:]
                n -= 1

            sum += int(''.join(max_digits))

        print(sum)

def find_max_in_string(s: str):
    if not s:
        return None, []
    max_digit = s[0]
    max_ids = [0]
    for i, ch in enumerate(s[1:], start=1):
        if ch > max_digit:
            max_digit = ch
            max_ids = [i]
        elif ch == max_digit:
            max_ids.append(i)
    return max_digit, max_ids
                
                
            

if __name__ == "__main__":
    main()