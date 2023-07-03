import random

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]


class Player():
    def __init__(self, role, name):
        self.role = role
        self.name = name

    def computer_move(self):
        for move in best_moves:
            if board[move] != "X" and board[move] != "O":
                board[move] = computer.role
                best_moves.remove(move)
                break
            else:
                pass

    def human_move(self):
        while True:
            number = int(input("Number: "))
            print()
            if number < 0 or number > 8:
                print("Choose another position")
                pass
            else:
                if board[number] != "X" and board[number] != "O":
                    board[number] = human.role
                    break


human = Player("X", "Human")
computer = Player("O", "Computer")


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_win(board, person):
    if board[0] == board[1] == board[2]:
        print(f"The winner is: {person.name}")
        return True
    elif board[3] == board[4] == board[5]:
        print(f"The winner is: {person.name}")
        return True
    elif board[6] == board[7] == board[8]:
        print(f"The winner is: {person.name}")
        return True
    elif board[0] == board[3] == board[6]:
        print(f"The winner is: {person.name}")
        return True
    elif board[1] == board[4] == board[7]:
        print(f"The winner is: {person.name}")
        return True
    elif board[2] == board[5] == board[8]:
        print(f"The winner is: {person.name}")
        return True
    elif board[0] == board[4] == board[8]:
        print(f"The winner is: {person.name}")
        return True
    elif board[2] == board[4] == board[6]:
        print(f"The winner is: {person.name}")
        return True
    else:

        return False


def instructions():
    print("""
    Choose number between 0 - 8
    """)


def game():
    choose = random.randint(0, 1)
    if choose == 0:
        print("Zacznie człowiek!")
        display_board(board)
        for i in range(5):
            human.human_move()
            win_human = check_win(board, human)
            if win_human:
                break
            computer.computer_move()
            win_computer = check_win(board, computer)
            if win_computer:
                break
            display_board(board)
        if win_computer == False and win_human == False:
            print("REMIS")
            print()
    if choose == 1:
        print("Zacznie komputer!")
        for i in range(5):
            computer.computer_move()
            display_board(board)
            win_computer = check_win(board, computer)
            if win_computer:
                break
            human.human_move()
            win_human = check_win(board, human)
            if win_human:
                break
        if win_computer == False and win_human == False:
            print("REMIS")
            print()


def main():
    instructions()
    game()
    display_board(board)


main()
