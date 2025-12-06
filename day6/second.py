from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    nums = []
    ops = []
    results = []

    columns = []
    
    with p.open() as f:
        for line in f:
            for i, char in enumerate(line):
                if len(columns) <= i:
                    columns.append([])
                columns[i].append(char)

    for col in columns:
        num = ''
        for char in col:
            if char.isdigit():
                num += char
            elif char in '+*':
                ops.append(char)
                nums.append([])
        if len(num) > 0:
            nums[-1].append(int(num))
            
    for i in range(len(nums)):
        if ops[i] == '+':
            result = sum(nums[i])
        elif ops[i] == '*':
            result = 1
            for n in nums[i]:
                result *= n
        results.append(result)
    
    sum_results = sum(results)
    print(sum_results)

if __name__ == "__main__":
    main()
