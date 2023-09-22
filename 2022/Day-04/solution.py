
def parseFile(file) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

#######################################################################
# part 1


count = 0
for line in parseFile("input.txt"):

    first_range, second_range = line.split(",")

    # first range
    i1, e1 = map(int, first_range.split("-"))
    # second range
    i2, e2 = map(int, second_range.split("-"))

    if i1-i2 >= 0 and e2-e1 >= 0:  # first range is smaller
        count += 1

    elif i2-i1 >= 0 and e1-e2 >= 0:  # second range is smaller
        count += 1

print(count)  # 571


#######################################################################
# part 2

count = 0
for line in parseFile("input.txt"):

    first_range, second_range = line.split(",")

    # first range
    i1, e1 = map(int, first_range.split("-"))
    # second range
    i2, e2 = map(int, second_range.split("-"))

    if e1 >= i2 and i1 < e2:
        count += 1
        continue

    if i1 <= e2 and i2 < e1:
        count += 1
        continue

print(count)  # 917
