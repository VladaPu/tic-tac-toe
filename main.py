def greet():
    print("--------------------")
    print("--Приветствуем вас--")
    print("-------в игре-------")
    print("  формат ввода: x y ")
    print("  x - номер строки  ")
    print("  y - номер столбца ")


field = [[" "] * 3 for i in range(3)]


def show():
    print()
    print("   │ 0 │ 1 │ 2 │")
    print("_______________")
    for i, row in enumerate(field):
        row_str = f" {i} │ {' │ '.join(row)} │"
        print(row_str)
        print("_______________")


def ask():
    while True:
        cords = input("    Ваш ход:").split()

        if len(cords) != 2:
            print("Введите две координаты!")
            continue

        x, y = cords

        if not (x.isdigit() or y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка занята")
        else:
            print("Значение вне диапазона")


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for cord in win_cord:
        symbols = []

        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True

        if symbols == ["O", "O", "O"]:
            print("Выиграл O!")
            return True

    return False


greet()

num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if num == 9:
        print("Ничья!")
        break
