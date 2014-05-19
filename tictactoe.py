class Board:
    def __init__(self, state=None):
        if state is None:
            state = ((None,) * 3,) * 3
        self.state = state
