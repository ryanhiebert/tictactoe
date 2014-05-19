from tictactoe import Board

def test_board_init():
    state = (
        (None, None, None),
        (None, None, None),
        (None, None, None),
    )
    board = Board(state)
    assert board.state == state

def test_default_init():
    state = (
        (None, None, None),
        (None, None, None),
        (None, None, None),
    )
    board = Board()
    assert board.state == state
