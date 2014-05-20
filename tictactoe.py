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
