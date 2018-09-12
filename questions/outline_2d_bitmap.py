import pprint

pp = pprint.PrettyPrinter()

bitmap = [[0, 0, 0, 0, 0, 0, 0, ],
          [0, 1, 1, 1, 0, 1, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0]]

pp.pprint(bitmap)

print("\n\n\n")

for x, line in enumerate(bitmap):
    for y, point in enumerate(line):
        try:
            if point in {1, 2} and \
                    bitmap[x - 1][y] in {1, 2} and \
                    bitmap[x + 1][y] in {1, 2} and \
                    bitmap[x][y - 1] in {1, 2} and \
                    bitmap[x][y + 1] in {1, 2}:
                bitmap[x][y] = 2
        except:
            pass

for x, line in enumerate(bitmap):
    for y, point in enumerate(line):
        if point == 2:
            bitmap[x][y] = 0

pp.pprint(bitmap)
