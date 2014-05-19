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

def test_player_turn():
    board = Board()
    assert board.turn() == 'x'

def test_play_square():
    board = Board()
    board = board.move('b0')
    assert board.state[1][0] == 'x'
