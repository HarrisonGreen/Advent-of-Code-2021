import numpy as np

def read_boards():
    file_name = "Data/day4_order.txt"
    file = open(file_name, "r")

    for line in file:
        order = list(map(int, line.split(",")))

    file_name = "Data/day4_boards.txt"
    file = open(file_name, "r")
    boards = []

    board = np.zeros([5, 5], dtype=int)
    row = 0

    for line in file:
        if line == "\n":
            boards.append(board)
            board = np.zeros([5, 5], dtype=int)
            row = 0
        else:
            board[row, :] = list(map(int, line.strip("\n").split()))
            row += 1

    boards.append(board)
    return boards, order

def winning_score(boards, order):
    pos = 0

    while True:
        for n in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if boards[n][i, j] == order[pos]:
                        boards[n][i, j] = -1

                        if sum(boards[n][i, :]) == -5 or sum(boards[n][:, j]) == -5:
                            return (boards[n].sum() + (boards[n] == -1).sum()) * order[pos]

        pos += 1

def losing_score(boards, order):
    pos = 0
    found = {i: False for i in range(len(boards))}

    while True:
        for n in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if boards[n][i, j] == order[pos]:
                        boards[n][i, j] = -1

                        if sum(boards[n][i, :]) == -5 or sum(boards[n][:, j]) == -5:
                            found[n] = True
                            if sum(found.values()) == len(boards):
                                return (boards[n].sum() + (boards[n] == -1).sum()) * order[pos]

        pos += 1

if __name__ == "__main__":
    boards, order = read_boards()
    print(f"Part one: {winning_score(boards, order)}")
    print(f"Part two: {losing_score(boards, order)}")
    