from pathlib import Path

def main():
    p = Path("input.txt")
    if not p.exists():
        print(f"Input file not found: {p}")
        return

    nums = []
    ops = []
    results = []
    
    with p.open() as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            if parts[0] == '+' or parts[0] == '*':
                for op in parts:
                    ops.append(op)
            else:
                if len(nums) == 0:
                    for num in parts:
                        nums.append([])

                for i, num in enumerate(parts):
                        nums[i].append(int(num))

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
