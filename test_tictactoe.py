def test_board_init():
    from tictactoe import Board 
    state = (
        (None, None, None),
        (None, None, None),
        (None, None, None),
    )
    board = Board(state)
    assert board.state == state

def test_default_init():
    from tictactoe import Board
    state = (
        (None, None, None),
        (None, None, None),
        (None, None, None),
    )
    board = Board()
    assert board.state == state
