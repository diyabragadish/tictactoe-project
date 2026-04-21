def print_position_guide():
    """
    Prints a guide showing how players should enter row and column positions.
    """
    print("\nPosition Guide:")
    print("    0   1   2")
    print("0   _ | _ | _")
    print("   ---+---+---")
    print("1   _ | _ | _")
    print("   ---+---+---")
    print("2   _ | _ | _")


def print_board(board):
    """
    Prints the current tic-tac-toe board with row and column numbers.
    """
    print("\nCurrent Board:")
    print("    0   1   2")
    for i in range(3):
        print(f"{i}   {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("   ---+---+---")


def check_winner(board, player):
    """
    Returns True if the given player has won, otherwise False.
    """
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_draw(board):
    """
    Returns True if the board is full and there is no winner.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_move(board, player_name, player_symbol):
    """
    Gets a valid move from the current player.
    """
    while True:
        try:
            row = int(input(f"{player_name} ({player_symbol}), enter row (0-2): "))
            col = int(input(f"{player_name} ({player_symbol}), enter column (0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
            elif board[row][col] != " ":
                print("That cell is already occupied. Try again.")
            else:
                return row, col

        except ValueError:
            print("Invalid input. Please enter whole numbers only.")


def print_score(player1_name, player2_name, scores):
    """
    Prints the current score for both players.
    """
    print("\nScoreboard:")
    print(f"{player1_name} (X): {scores['X']}")
    print(f"{player2_name} (O): {scores['O']}")


def play_game():
    """
    Runs the Tic-Tac-Toe game with replay and score tracking.
    """
    player1_name = input("Enter name for Player X: ")
    player2_name = input("Enter name for Player O: ")

    scores = {"X": 0, "O": 0}

    print_position_guide()

    while True:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        current_player = "X"

        print("\nWelcome to Tic-Tac-Toe!")
        print_score(player1_name, player2_name, scores)

        while True:
            print_board(board)

            if current_player == "X":
                player_name = player1_name
            else:
                player_name = player2_name

            row, col = get_move(board, player_name, current_player)
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"\nCongratulations! {player_name} ({current_player}) wins!")
                scores[current_player] += 1
                break

            if is_draw(board):
                print_board(board)
                print("\nIt's a draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        print_score(player1_name, player2_name, scores)

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("\nFinal Scores:")
            print_score(player1_name, player2_name, scores)
            print("Thanks for playing!")
            break


play_game()