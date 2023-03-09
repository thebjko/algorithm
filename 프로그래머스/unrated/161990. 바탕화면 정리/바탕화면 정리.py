def solution(wallpaper):
    ls = [[], []]
    for idx_y, line in enumerate(wallpaper):
        for idx_x, char in enumerate(line):
            if char == '#':
                ls[0].append(idx_x)
                ls[1].append(idx_y)
            
    return [min(ls[1]), min(ls[0]), max(ls[1])+1, max(ls[0])+1]