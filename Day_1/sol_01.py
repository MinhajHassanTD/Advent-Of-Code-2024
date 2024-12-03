''' --- Day 1: Historian Hysteria --- '''

filename = "Day_1/input_01.txt"
with open(filename, 'r') as file:
    content = file.read()

lines = content.splitlines()
lst1 = [int(i.split()[0]) for i in lines]
lst2 = [int(i.split()[1]) for i in lines]

lst1.sort()
lst2.sort()

part_1 = sum([abs(lst1[i] - lst2[i]) for i in range(len(lst1))])
part_2 = sum([lst1[i] * lst2.count(lst1[i]) for i in range(len(lst1)) if lst1[i] in lst2])

print(f"Part 1 : {part_1}")
print(f"Part 2 : {part_2}")