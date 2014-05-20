class Board:
    def __init__(self, state=None):
        if state is None:
            state = ((None,) * 3,) * 3
        self.state = state

    def turn(self):
        x = o = 0
        for row in self.state:
            for space in row:
                if space == 'x':
                    x += 1
                elif space == 'o':
                    o += 1

        if x <= o:
            return 'x'
        else:
            return 'o'

    def move(self, move):
        state = [list(row) for row in self.state]

        turn = self.turn()

        row = 'abc'.index(move[0])
        col = '012'.index(move[1])

        state[row][col] = turn

        state = tuple(tuple(row) for row in state)

        return Board(state)
