from copy import copy

def deterministic_game(positions):
    dice_num = 1
    scores = [0, 0]
    rolls = 0

    while True:
        for player in (0, 1):
            rolls += 3
            roll, dice_num = roll_dice(dice_num)
            positions[player] = (positions[player] + roll - 1)%10 + 1
            scores[player] += positions[player]

            if scores[player] >= 1000:
                return rolls * scores[1 - player]

def roll_dice(dice_num):
    roll = 0
    for _ in range(3):
        roll += dice_num
        dice_num = dice_num%100 + 1
    return roll, dice_num

def quantum_game(positions):
    games = {0: {(positions[0], positions[1], 0, 0): 1}}
    rolls = 0
    counts = [0, 0]

    while len(games[rolls]) > 0:
        player = (rolls//3)%2
        games[rolls + 3] = {}

        for state, n in games[rolls].items():
            for i in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):

                new_state = list(state)
                new_state[player] = (new_state[player] + i[0] - 1)%10 + 1
                new_state[player + 2] += new_state[player]
                new_state = tuple(new_state)
                m = n * i[1]

                if new_state[player + 2] >= 21:
                    counts[player] += m
                else:
                    games[rolls + 3][new_state] = games[rolls + 3].get(new_state, 0)
                    games[rolls + 3][new_state] += m

        rolls += 3

    return max(counts)

if __name__ == "__main__":
    positions = [8, 9]
    print(f"Part one: {deterministic_game(copy(positions))}")
    print(f"Part two: {quantum_game(copy(positions))}")
