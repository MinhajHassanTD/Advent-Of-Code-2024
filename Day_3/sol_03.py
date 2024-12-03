''' --- Day 3: Mull It Over --- '''

import re

filename = "Day_3/input_03.txt"
with open(filename, 'r') as file:
    content = file.read()

mul = re.findall(r"mul\((\d+),(\d+)\)", content)
instructions = re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content)

mul_enabled = True
sums = 0

for i in instructions:
    instr = i.group()

    if instr.startswith("mul"):
        if mul_enabled:
            a, b = map(int, re.findall(r"\d+", instr))
            sums += a * b

    elif instr == "do()":
        mul_enabled = True

    elif instr == "don't()":
        mul_enabled = False

print(f'Part 1: {sum([int(a) * int(b) for a, b in mul])}')
print(f'Part 2: {sums}')