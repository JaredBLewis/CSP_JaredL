# Jared Lewis, Tick Tack Toe Python


def print_board(board):
    print("  1 2 3")
    print("1 " + board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("  -----")
    print("2 " + board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("  -----")
    print("3 " + board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def main():

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    winner = None

    while winner is None:
        print_board(board)
        print("Player " + player + "'s turn.")
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ") - 1)

        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That space is already taken.")

        winner = check_winner(board)

    print_board(board)
    print("Player " + winner + " wins!")

if __name__ == "__main__":
    main()

