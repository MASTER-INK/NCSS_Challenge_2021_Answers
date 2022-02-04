import collections
##setup
with open("patches.txt") as haha:
    line = []
    for i in haha:
        line.append(i.strip())
    paint_spots = collections.defaultdict(list)
    for i in line:
        n = 0
        for p in i:
            n += 1
            if p == "%":
                paint_spots[line.index(i)] += str(n)


last_line = []
for lines in paint_spots:
    for k in sorted(paint_spots[lines]):
        if k in last_line and str(int(k) + 1) in paint_spots[lines] and str(int(k) - 1) in paint_spots[lines]:
            print((lines, k))
    last_line = paint_spots[lines]
