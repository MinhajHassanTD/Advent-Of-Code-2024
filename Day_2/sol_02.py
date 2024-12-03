''' --- Day 2: Red-Nosed Reports --- '''

filename = "Day_2/input_02.txt"
with open(filename, 'r') as file:
    content = file.read()

safe_1 = 0
safe_2 = 0
reports = content.splitlines()

def isSafe(levels):
    inc = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    dec = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    if not(inc or dec):
        return False
    
    difference = [abs(levels[i + 1] - levels[i]) for i in range(len(levels) - 1)]
    if max(difference) > 3 or min(difference) < 1:
        return False
    
    return True

for report in reports:
    levels = [int(x) for x in report.split()]
    if isSafe(levels):
        safe_1 += 1
        safe_2 += 1
    else:
        for i in range(len(levels)):
            level = levels[:i] + levels[i + 1:]
            if isSafe(level):
                safe_2 += 1
                break

print(f"Part 1 : {safe_1}")
print(f"Part 2 : {safe_2}")