class Board:
    def __init__(self, state):
        self.state = state

def main():
    board = Board(
        ((None,) * 3,) * 3
    )
    for row in board.state:
        print(row)

if __name__ == '__main__':
    main()