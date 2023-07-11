
def parse(file):
    with open(file) as f:
        return f.read().splitlines()


def priority(ch):
    code = ord(ch)
    return code - 96 if ord(ch) > 90 else code - 38


data = parse("input.txt")
l = len(data)

# ------------------ Part 1 ----------------------

total = 0

for rucksack in data:
    n = len(rucksack)
    first, second = set(rucksack[:n//2]), set(rucksack[n//2:])
    item = first.intersection(second).pop()
    total += priority(item)

print(total)


# ------------------ Part 2 ----------------------

total = 0

for i in range(0, l, 3):
    g1, g2, g3 = set(data[i]), set(data[i+1]), set(data[i+2])
    item = g1.intersection(g2).intersection(g3).pop()
    total += priority(item)

print(total)
