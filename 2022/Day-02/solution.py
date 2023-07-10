
file = open("input.txt", "r")
inputs = file.read().split("\n")
file.close()


def convert(x):
    return ord(x) - 64 if ord(x) < 68 else ord(x) - 87

# ----------------- Part 1 -------------------

# X -> Rock -> 1
# Y -> Paper -> 2
# Z -> Scissors -> 3


guide = [tuple(map(convert, data.split(" "))) for data in inputs]

outcomeOf = {
    (1, 2): 6,
    (2, 3): 6,
    (3, 1): 6,
    (1, 1): 3,
    (2, 2): 3,
    (3, 3): 3,
    (1, 3): 0,
    (3, 2): 0,
    (2, 1): 0
}

total_points = 0

for move in guide:
    total_points += (3 + move[1]) if (move[0] == move[1]
                                      ) else (outcomeOf[move] + move[1])

print(total_points)


# ----------------- Part 2 -------------------

# X -> Lose -> 1 (key value of Losing moves in movesFor)
# Y -> Draw -> 2 (key value of Tie moves in movesFor)
# Z -> Win -> 3 (key value of Win moves in movesFor)

movesFor = {
    1: [3, 1, 2],  # Lose moves
    2: [1, 2, 3],  # Draw moves
    3: [2, 3, 1]  # Win moves
}

total_points = 0

for pair in guide:
    theirMove, outcome = pair
    myMove = movesFor[outcome][theirMove - 1]
    total_points += (outcomeOf[(theirMove, myMove)] + myMove)


print(total_points)
