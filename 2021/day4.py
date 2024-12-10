numbers = None
boards = []
board = []
fill = []
with open('day4.txt') as f:
    for line in f:
        line = line.strip()
        if numbers is None:
            numbers = [int(x) for x in line.split(',')]
        else:
            if line:
                board.append([int(x) for x in line.split()])
            else:
                if board:
                    boards.append(board)
                board = []
for b in boards:
    fill.append([[False for _ in range(5)] for _ in range(5)])
onestar = False
winBoards = [False for _ in range(len(boards))]
for num in numbers:
    for i,b in enumerate(boards):
        if winBoards[i]:
            continue
        for r in range(5):
            for c in range(5):
                if b[r][c] == num:
                    fill[i][r][c] = True
        won = False
        for r in range(5):
            ok = True
            for c in range(5):
                if not fill[i][r][c]:
                    ok = False
            if ok:
                won = True
        for c in range(5):
            ok = True
            for r in range(5):
                if not fill[i][r][c]:
                    ok = False
            if ok:
                won = True
        if won:
            winBoards[i] = True
            if not onestar or all([winBoards[h] for h in range(len(boards))]):
                unmarked = 0
                for c in range(5):
                    for r in range(5):
                        if not fill[i][r][c]:
                            unmarked+=b[r][c]
                print(unmarked*num)
                onestar=True