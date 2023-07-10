# ---------------- PART 1 --------------------

file = open("input.txt", "r")

# splitting the input into each elf callories
content = file.read().split("\n\n")
file.close()

# sum the total calories with each elf
calories = []
for elf in content:
    elf = [int(calories) for calories in elf.split("\n")]
    calories.append(sum(elf))

# print the maximum of calories
print(max(calories))


# ---------------- PART 2 --------------------

calories.sort(reverse=True)

# sum of the largest 3 calories
print(sum(calories[:3]))
