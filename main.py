
import turtle
import random

board = [['', '', ''], ['', '', ''], ['', '', '']]
# move number
n = [0]
# P(Player vs Player) or B(Player vs Bot)
opponent = ['']
# Who goes first(Player vs Bot)
first = ['']
# player(X/O)
p = ['']
# bot(X/O)
b = ['']


def home(x, y):
    # data reset
    for i in range(3):
        for j in range(3):
            board[i][j] = ''
    n[0] = 0
    opponent[0] = ''
    first[0] = ''
    b[0] = ''
    p[0] = ''

    # menu
    turtle.hideturtle()
    turtle.speed(0)
    turtle.clear()
    turtle.title("Tic-Tac-Toe")
    draw_home()
    turtle.onscreenclick(home_select)
    turtle.mainloop()


def home_select(x, y):
    # Creating button for start game.
    if 0 >= x >= -35 >= y >= -200:
        opponent_menu()


def opponent_menu():
    draw_opponent_menu()
    turtle.onscreenclick(opponent_select)
    turtle.mainloop()


def opponent_select(x, y):
    # Player vs Bot
    if -180 <= x <= -90 and -170 <= y <= -150:
        opponent[0] = "B"
        player_vs_bot_menu()
    # Player vs Player
    elif 90 <= x <= 190 and -170 <= y <= -150:
        opponent[0] = "P"
        start()


def player_vs_bot_menu():
    draw_player_vs_bot_menu()
    turtle.onscreenclick(player_vs_bot_select)
    turtle.mainloop()


def player_vs_bot_select(x, y):
    # Bot
    if -90 >= x >= -150 >= y >= -170:
        first[0] = "B"
        b[0] = "X"
        p[0] = "O"
        start()
    # Player
    elif 90 <= x <= 160 and -170 <= y <= -150:
        first[0] = "P"
        b[0] = "O"
        p[0] = "X"
        start()


def start():
    draw_board()
    # Player vs Bot(first)
    if opponent[0] == "B" and first[0] == "B":
        bot()
    turtle.onscreenclick(play)
    turtle.mainloop()


def play(x, y):
    # 1
    if -150 <= x <= -50 and 50 <= y <= 150:
        if board[0][0] == '':
            if n[0] % 2 == 0:
                board[0][0] = "X"
                n[0] = n[0] + 1
                cross(-140, 140)
            else:
                board[0][0] = "O"
                n[0] = n[0] + 1
                circle(-60, 100)

    # 2
    elif -50 <= x <= 50 and 50 <= y <= 150:
        if board[0][1] == '':
            if n[0] % 2 == 0:
                board[0][1] = "X"
                n[0] = n[0] + 1
                cross(-40, 140)
            else:
                board[0][1] = "O"
                n[0] = n[0] + 1
                circle(40, 100)

    # 3
    elif 50 <= x <= 150 and 50 <= y <= 150:
        if board[0][2] == '':
            if n[0] % 2 == 0:
                board[0][2] = "X"
                n[0] = n[0] + 1
                cross(60, 140)
            else:
                board[0][2] = "O"
                n[0] = n[0] + 1
                circle(140, 100)

    # 4
    elif -150 <= x <= -50 <= y <= 50:
        if board[1][0] == '':
            if n[0] % 2 == 0:
                board[1][0] = "X"
                n[0] = n[0] + 1
                cross(-140, 40)
            else:
                board[1][0] = "O"
                n[0] = n[0] + 1
                circle(-60, 0)

    # 5
    elif -50 <= x <= 50 and -50 <= y <= 50:
        if board[1][1] == '':
            if n[0] % 2 == 0:
                board[1][1] = "X"
                n[0] = n[0] + 1
                cross(-40, 40)
            else:
                board[1][1] = "O"
                n[0] = n[0] + 1
                circle(40, 0)

    # 6
    elif 50 <= x <= 150 and y >= -50 and y <= 50:
        if board[1][2] == '':
            if n[0] % 2 == 0:
                board[1][2] = "X"
                n[0] = n[0] + 1
                cross(60, 40)
            else:
                board[1][2] = "O"
                n[0] = n[0] + 1
                circle(140, 0)

    # 7
    elif -150 <= x <= -50 and -150 <= y <= -50:
        if board[2][0] == '':
            if n[0] % 2 == 0:
                board[2][0] = "X"
                n[0] = n[0] + 1
                cross(-140, -60)
            else:
                board[2][0] = "O"
                n[0] = n[0] + 1
                circle(-60, -100)

    # 8
    elif 50 >= x >= -50 >= y >= -150:
        if board[2][1] == '':
            if n[0] % 2 == 0:
                board[2][1] = "X"
                n[0] = n[0] + 1
                cross(-40, -60)
            else:
                board[2][1] = "O"
                n[0] = n[0] + 1
                circle(40, -100)

    # 9
    elif 50 <= x <= 150 and -150 <= y <= -50:
        if board[2][2] == '':
            if n[0] % 2 == 0:
                board[2][2] = "X"
                n[0] = n[0] + 1
                cross(60, -60)
            else:
                board[2][2] = "O"
                n[0] = n[0] + 1
                circle(140, -100)
    # check if someone won
    score()

    # Player vs Bot
    if opponent[0] == "B":
        if first[0] == "B" and n[0] % 2 == 0:
            bot()
        elif first[0] == "P" and n[0] % 2 == 1:
            bot()


def bot():
    # vertical
    board_vertical = [[board[j][i] for j in range(3)] for i in range(3)]
    # diagonal
    board_diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    board_diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    # first
    if n[0] == 0:
        move = random.randint(1, 5)
        # corner
        if move == 1:
            play(-100, 100)
        elif move == 2:
            play(100, 100)
        elif move == 3:
            play(-100, -100)
        elif move == 4:
            play(100, -100)
        # center
        elif move == 5:
            play(0, 0)

    # second
    elif n[0] == 1:
        if board[1][1] == "":
            play(0, 0)
        else:
            move = random.randint(1, 4)
            # corner
            if move == 1:
                play(-100, 100)
            elif move == 2:
                play(100, 100)
            elif move == 3:
                play(-100, -100)
            elif move == 4:
                play(100, -100)

    # win_horizontal
    elif board[0] == [b[0], b[0], ""]:
        play(100, 100)
    elif board[0] == [b[0], "", b[0]]:
        play(0, 100)
    elif board[0] == ["", b[0], b[0]]:
        play(-100, 100)

    elif board[1] == [b[0], b[0], ""]:
        play(100, 0)
    elif board[1] == [b[0], "", b[0]]:
        play(0, 0)
    elif board[1] == ["", b[0], b[0]]:
        play(-100, 0)

    elif board[2] == [b[0], b[0], ""]:
        play(100, -100)
    elif board[2] == [b[0], "", b[0]]:
        play(0, -100)
    elif board[2] == ["", b[0], b[0]]:
        play(-100, -100)

        # win_vertical
    elif board_vertical[0] == [b[0], b[0], ""]:
        play(-100, -100)
    elif board_vertical[0] == [b[0], "", b[0]]:
        play(-100, 0)
    elif board_vertical[0] == ["", b[0], b[0]]:
        play(-100, 100)

    elif board_vertical[1] == [b[0], b[0], ""]:
        play(0, -100)
    elif board_vertical[1] == [b[0], "", b[0]]:
        play(0, 0)
    elif board_vertical[1] == [b[0], b[0], b[0]]:
        play(0, 100)

    elif board_vertical[2] == [b[0], b[0], ""]:
        play(100, -100)
    elif board_vertical[2] == [b[0], "", b[0]]:
        play(100, 0)
    elif board_vertical[2] == ["", b[0], b[0]]:
        play(100, 100)

        # win_diagonal
    elif board_diagonal_1 == [b[0], b[0], ""]:
        play(100, -100)
    elif board_diagonal_1 == [b[0], "", b[0]]:
        play(0, 0)
    elif board_diagonal_1 == ["", b[0], b[0]]:
        play(-100, 100)

    elif board_diagonal_2 == [b[0], b[0], ""]:
        play(-100, -100)
    elif board_diagonal_2 == [b[0], "", b[0]]:
        play(0, 0)
    elif board_diagonal_2 == ["", b[0], b[0]]:
        play(100, 100)

        # block_vertical
    elif board[0] == [p[0], p[0], ""]:
        play(100, 100)
    elif board[0] == [p[0], "", p[0]]:
        play(0, 100)
    elif board[0] == ["", p[0], p[0]]:
        play(-100, 100)

    elif board[1] == [p[0], p[0], ""]:
        play(100, 0)
    elif board[1] == [p[0], "", p[0]]:
        play(0, 0)
    elif board[1] == ["", p[0], p[0]]:
        play(-100, 0)

    elif board[2] == [p[0], p[0], ""]:
        play(100, -100)
    elif board[2] == [p[0], "", p[0]]:
        play(0, -100)
    elif board[2] == ["", p[0], p[0]]:
        play(-100, -100)

        # block_horizontal
    elif board_vertical[0] == [p[0], p[0], ""]:
        play(-100, -100)
    elif board_vertical[0] == [p[0], "", p[0]]:
        play(-100, 0)
    elif board_vertical[0] == ["", p[0], p[0]]:
        play(-100, 100)

    elif board_vertical[1] == [p[0], p[0], ""]:
        play(0, -100)
    elif board_vertical[1] == [p[0], "", p[0]]:
        play(0, 0)
    elif board_vertical[1] == ["", p[0], p[0]]:
        play(0, 100)

    elif board_vertical[2] == [p[0], p[0], ""]:
        play(100, -100)
    elif board_vertical[2] == [p[0], "", p[0]]:
        play(100, 0)
    elif board_vertical[2] == ["", p[0], p[0]]:
        play(100, 100)

    # block_diagonal
    elif board_diagonal_1 == [p[0], p[0], ""]:
        play(100, -100)
    elif board_diagonal_1 == [p[0], "", p[0]]:
        play(0, 0)
    elif board_diagonal_1 == ["", p[0], p[0]]:
        play(-100, 100)

    elif board_diagonal_2 == [p[0], p[0], ""]:
        play(-100, -100)
    elif board_diagonal_2 == [p[0], "", p[0]]:
        play(0, 0)
    elif board_diagonal_2 == ["", p[0], p[0]]:
        play(100, 100)

    # corner
    elif board[0][2] == "":
        play(100, 100)
    elif board[2][0] == "":
        play(-100, -100)
    elif board[2][2] == "":
        play(100, -100)
    elif board[0][0] == "":
        play(-100, 100)
    # center
    elif board[1][1] == "":
        play(0, 0)
    # sides
    elif board[0][1] == "":
        play(0, 100)
    elif board[1][0] == "":
        play(-100, 0)
    elif board[1][2] == "":
        play(100, 0)
    elif board[2][1] == "":
        play(0, -100)


def score():
    # horizontal
    for i in range(3):
        if board[i] == ["X", "X", "X"]:
            line(-150, 100 - 100 * i, 150, 100 - 100 * i, "red")
            winner_p1()
        elif board[i] == ["O", "O", "O"]:
            line(-150, 100 - 100 * i, 150, 100 - 100 * i, "green")
            winner_p2()

    # vertical
    for i in range(3):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            line(-100 + 100 * i, 150, -100 + 100 * i, -150, "red")
            winner_p1()
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            line(-100 + 100 * i, 150, -100 + 100 * i, -150, "green")
            winner_p2()

    # diagonal
    for i in range(2):
        if board[0][0 + (2 * i)] == "X" and board[1][1] == "X" and board[2][2 - (2 * i)] == "X":
            line(-150 + 300 * i, 150, 150 - 300 * i, -150, "red")
            winner_p1()
        elif board[0][0 + (2 * i)] == "O" and board[1][1] == "O" and board[2][2 - (2 * i)] == "O":
            line(-150 + 300 * i, 150, 150 - 300 * i, -150, "green")
            winner_p2()

    # draw
    if n[0] == 9:
        draw()


def winner_p1():
    turtle.onscreenclick(None)
    turtle.pu()
    turtle.goto(0, 200)
    turtle.color("red")
    if opponent[0] == "B" and first[0] == "B":
        turtle.write("Bot won this game", align="center", font=("Futura", 30))
    else:
        turtle.write("Player 1 won this game", align="center", font=("Futura", 30))
    turtle.goto(250, -200)
    turtle.write("(Click anywhere to return to the main menu)", align="right", font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()


def winner_p2():
    turtle.onscreenclick(None)
    turtle.pu()
    turtle.goto(0, 200)
    turtle.color("Green")
    if opponent[0] == "B" and first[0] == "P":
        turtle.write("Bot won this game", align="center", font=("Futura", 30))
    else:
        turtle.write("Player 2 won this game", align="center", font=("Futura", 30))
    turtle.goto(250, -200)
    turtle.write("(Click anywhere to return to the main menu)", align="right", font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()


def draw():
    turtle.onscreenclick(None)
    turtle.color("Blue")
    turtle.pu()
    turtle.goto(0, 200)
    turtle.write("Draw", align="center", font=("Futura", 30))
    turtle.goto(250, -200)
    turtle.write("(Click anywhere to return to the main menu)", align="right", font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()


def menu_button(a, b, c, d1, d2):
    turtle.pu()
    turtle.goto(a, b)
    turtle.setheading(0)
    turtle.pd()
    turtle.color(c)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(d1)
        turtle.right(90)
        turtle.forward(d2)
        turtle.right(90)
    turtle.end_fill()


def cross(a, b):
    turtle.color("red")
    turtle.pu()
    turtle.goto(a, b)
    turtle.pd()
    turtle.goto(a + 80, b - 80)
    turtle.pu()
    turtle.goto(a + 80, b)
    turtle.pd()
    turtle.goto(a, b - 80)


def circle(a, b):
    turtle.color("green")
    turtle.pu()
    turtle.goto(a, b)
    turtle.pd()
    turtle.setheading(90)
    turtle.circle(40)


def line(a1, b1, a2, b2, c):
    turtle.pu()
    turtle.goto(a1, b1)
    turtle.color(c)
    turtle.pd()
    turtle.pensize(10)
    turtle.goto(a2, b2)


def draw_home():
    turtle.pu()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("Tic-Tac-Toe", align="center", font=("Futura", 30))

    menu_button(-35, -150, "blue", 70, 20)
    turtle.pu()
    turtle.goto(0, -170)
    turtle.color("grey")
    turtle.write("Play", align="center", font=(10))


def draw_opponent_menu():
    turtle.clear()
    turtle.pu()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("Choose your opponent", align="center", font=("Futura", 30))

    # Player vs Bot
    menu_button(-180, -150, "blue", 100, 20)
    turtle.pu()
    turtle.goto(-130, -170)
    turtle.color("grey")
    turtle.write("Player vs Bot", align="center", font=(10))

    # Player vs Player
    menu_button(90, -150, "blue", 100, 20)
    turtle.pu()
    turtle.goto(140, -170)
    turtle.color("grey")
    turtle.write("Player vs Player", align="center", font=(10))


def draw_player_vs_bot_menu():
    turtle.clear()
    turtle.pu()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("Who goes first?", align="center", font=("Futura", 30))

    # button1
    menu_button(-150, -150, "blue", 70, 20)
    turtle.pu()
    turtle.goto(-115, -170)
    turtle.color("grey")
    turtle.write("Bot", align="center", font=(10))

    # button2
    menu_button(90, -150, "blue", 70, 20)
    turtle.pu()
    turtle.goto(125, -170)
    turtle.color("grey")
    turtle.write("Player", align="center", font=(10))


def draw_board():
    turtle.clear()
    turtle.color("black")
    turtle.pensize(5)

    # horizontal
    for i in range(2):
        turtle.pu()
        turtle.goto(-150, 50 - 100 * i)
        turtle.setheading(0)
        turtle.pd()
        turtle.forward(300)

    # vertical
    for i in range(2):
        turtle.pu()
        turtle.goto(-50 + 100 * i, 150)
        turtle.setheading(270)
        turtle.pd()
        turtle.forward(300)


if __name__ == '__main__':
    home(0, 0)
