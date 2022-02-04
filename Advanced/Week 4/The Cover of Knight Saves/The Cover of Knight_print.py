def new_moves(pos, xtrue, x, y, new_negative):
    types = [1 * pos, 2 * pos]
    if new_negative and pos == -1:
        types = [1 * pos, 2 * pos * pos]
    elif new_negative and pos == 1:
        types = [1 * pos * pos, 2 * pos]
    elif new_negative == False and xtrue == False:
        if pos == -1:
            types = [1, 2 * pos]
        else:
            types = [1 * -1, 2 * -1]
    elif new_negative == False and xtrue:
        if pos == 1:
            types = [1, -2]
    if xtrue == True:
        new_pos = x + types[0], y + types[1]
    else:
        new_pos = x + types[1], y + types[0]
    return new_pos
def move_calc(m, place_list):
    print(place_list)
    new_place_list = []
    for numbers_list in place_list:
        x, y = numbers_list
        pos_times = [1, 3, 5, 7]
        xtrue_times = [0, 1, 4, 5]
        new_negative_times = [0, 1, 2, 3]
        for tk in range(8):
            if tk in pos_times:
                pos = 1
            else:
                pos = -1
            if tk in xtrue_times:
                xtrue = True
            else:
                xtrue = False
            if tk in new_negative_times:
                new_negative = True
            else:
                new_negative = False
            print("POS:", pos, "xtrue:", xtrue, "New_Negative:", new_negative)
            new_x, new_y = new_moves(pos, xtrue, x, y, new_negative)
            if new_x >= 0 and new_y >= 0:
                print(new_x, new_y)
                if new_x < len(grid) and new_y < len(grid) and grid[new_x][new_y] == ".":
                    grid[new_x][new_y] = str(m)
                for i in grid:
                  print(" ".join(i))
                ps = new_x, new_y
                print(ps)
                if ps not in place_list:
                    new_place_list.append(ps)
    return new_place_list

size = int(input("Size: "))
m = int(input("Moves: "))
placex, placey = input("Knight: ").split(",")
placey = int(placey)
placex = int(placex)
grid = [["."] * size for i in range(size)]
grid[placex][placey] = "0"
place_list = []
ps = placex, placey
place_list.append(ps)
free = ""
newest_ls = [(placex, placey)]
for i in grid:
  print(" ".join(i))
for i in grid:
    for y in i:
        free += y
for i in range(m):
    if "." in free:
        free = ""
        new_list_places = move_calc(i + 1, newest_ls)
        newest_ls = []
        for c in new_list_places:
            place_list.append(c)
            newest_ls.append(c)
        for i in grid:
            for y in i:
                free += y
for k in range(4):
    print()
for i in grid:
  print(" ".join(i))
