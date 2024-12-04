
def solve_a(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    grid = list(map(list, lines))
    potential_starts = []
    for line_idx, line in enumerate(grid):
        for col_idx, char in enumerate(line):
            if char == 'X':
                potential_starts.append(tuple([line_idx, col_idx]))

    return sum(map(lambda x: find_xmas(grid, x), potential_starts))

def find_xmas(grid: list[list[str]], t: tuple[int, int]) -> int:
    matches = 0
    if check_lr(grid, t):
        matches +=1
    if check_rl(grid, t):
        matches +=1
    if check_tb(grid, t):
        matches +=1
    if check_bt(grid, t):
        matches +=1
    if check_tl_br(grid, t):
        matches +=1
    if check_tr_bl(grid, t):
        matches +=1
    if check_bl_tr(grid, t):
        matches +=1
    if check_br_tl(grid, t):
        matches +=1

    return matches

def check_lr(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = grid[t[0]]
    if t[1]+1 >= row.__len__() or row[t[1]+1] != 'M':
        return False
    if t[1]+2 >= row.__len__() or row[t[1]+2] != 'A':
        return False
    if t[1]+3 >= row.__len__() or row[t[1]+3] != 'S':
        return False
    return True

def check_rl(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = grid[t[0]]
    if t[1]-1 < 0 or row[t[1]-1] != 'M':
        return False
    if t[1]-2 < 0 or row[t[1]-2] != 'A':
        return False
    if t[1]-3 < 0 or row[t[1]-3] != 'S':
        return False
    return True

def check_tb(grid: list[list[str]], t: tuple[int, int]) -> bool:
    if t[0]+1 >= grid.__len__() or grid[t[0]+1][t[1]] != 'M':
        return False
    if t[0]+2 >= grid.__len__() or  grid[t[0]+2][t[1]] != 'A':
        return False
    if t[0]+3 >= grid.__len__() or  grid[t[0]+3][t[1]] != 'S':
        return False
    return True


def check_bt(grid: list[list[str]], t: tuple[int, int]) -> bool:
    if t[0]-1 < 0 or grid[t[0]-1][t[1]] != 'M':
        return False
    if t[0]-2 < 0 or grid[t[0]-2][t[1]] != 'A':
        return False
    if t[0]-3 < 0 or grid[t[0]-3][t[1]] != 'S':
        return False
    return True

def check_tl_br(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = t[0]
    col = t[1]
    if row + 1 >= grid.__len__() or col + 1 >= grid[0].__len__() or grid[row +1][col +1] != 'M':
        return False
    if row + 2 >= grid.__len__() or col + 2 >= grid[0].__len__() or grid[row +2][col +2] != 'A':
        return False
    if row + 3 >= grid.__len__() or col + 3 >= grid[0].__len__() or grid[row +3][col +3] != 'S':
        return False
    return True

def check_tr_bl(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = t[0]
    col = t[1]
    if row + 1 >= grid.__len__() or col - 1 < 0 or grid[row +1][col -1] != 'M':
        return False
    if row + 2 >= grid.__len__() or col - 2 < 0 or grid[row +2][col -2] != 'A':
        return False
    if row + 3 >= grid.__len__() or col - 3 < 0 or grid[row +3][col -3] != 'S':
        return False
    return True

def check_bl_tr(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = t[0]
    col = t[1]
    if row - 1 < 0 or col +1 >= grid[0].__len__() or grid[row -1][col +1] != 'M':
        return False
    if row - 2 < 0 or col +2 >= grid[0].__len__() or grid[row -2][col +2] != 'A':
        return False
    if row - 3 < 0 or col +3 >= grid[0].__len__() or grid[row -3][col +3] != 'S':
        return False
    return True

def check_br_tl(grid: list[list[str]], t: tuple[int, int]) -> bool:
    row = t[0]
    col = t[1]
    if row -1 < 0 or col - 1 < 0 or grid[row -1][col -1] != 'M':
        return False
    if row -2 < 0 or col - 2 < 0 or grid[row -2][col -2] != 'A':
        return False
    if row -3 < 0 or col - 3 < 0 or grid[row -3][col -3] != 'S':
        return False
    return True

def solve_b(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    grid = list(map(list, lines))
    potential_starts = []
    for line_idx, line in enumerate(grid):
        for col_idx, char in enumerate(line):
            if char == 'A':
                potential_starts.append(tuple([line_idx, col_idx]))

    return sum(map(lambda x: find_mas_x(grid, x), potential_starts))

def find_mas_x(grid: list[list[str]], t: tuple[int, int]) -> int:
    tl = 'x' if not (t[0]-1 >= 0 and t[1]-1 >= 0) else grid[t[0]-1][t[1]-1]
    tr = 'x' if not (t[0]-1 >= 0 and t[1]+1 < grid[t[0]-1].__len__()) else grid[t[0]-1][t[1]+1]

    bl = 'x' if not (t[0]+1 < grid.__len__() and t[1]-1 >= 0) else grid[t[0]+1][t[1]-1]
    br = 'x' if not (t[0]+1 < grid.__len__() and t[1]+1 < grid[t[0]+1].__len__()) else grid[t[0]+1][t[1]+1]

    if (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M'):
        if (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'):
            return 1
    return 0


if __name__ == '__main__':
    print(solve_a('input'))
    print(solve_b('input'))