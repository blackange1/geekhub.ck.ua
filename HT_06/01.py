from time import sleep


MAX_SPACE = 5
colors = ['red', 'yellow' ,'green']
NEXT_INDEX = max(map(len, colors)) + MAX_SPACE


def print_colors(col_1, col_2, repeat=2 , delay=1):
    global NEXT_INDEX

    for _ in range(repeat):
        print(col_1.title(), end='')
        print(' ' * (NEXT_INDEX - len(col_1)), end='')
        print(col_2.title())

        sleep(delay)

    return None

r, y, g = colors
while True:
    print_colors(r, g, 4)
    print_colors(y, g)
    print_colors(g, r, 4)
    print_colors(y, r)
