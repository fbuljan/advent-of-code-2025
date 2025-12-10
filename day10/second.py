import re
from pathlib import Path
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, LpStatus, PULP_CBC_CMD

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

            raw_buttons = re.findall(r"\(([^()]*)\)", line)
            buttons = [
                [int(x) for x in part.split(",") if x.strip()]
                for part in raw_buttons
            ]

            jolts_str = re.search(r"\{(.*?)\}", line).group(1)
            target = [int(x) for x in jolts_str.split(",") if x.strip()]

            num_counters = len(target)
            num_buttons = len(buttons)
            
            if all(t == 0 for t in target):
                return 0
            
            prob = LpProblem("config", LpMinimize)

            x = [LpVariable(f"x_{j}", lowBound=0, cat=LpInteger) for j in range(num_buttons)]
            prob += lpSum(x)
            
            for i in range(num_counters):
                prob += lpSum(x[j] for j in range(num_buttons) if i in buttons[j]) == target[i]
            
            prob.solve(PULP_CBC_CMD(msg=0))
            
            if LpStatus[prob.status] == "Optimal":
                presses = int(round(sum(v.varValue for v in x)))

            result += presses
    
    print(result)


if __name__ == "__main__":
    main()