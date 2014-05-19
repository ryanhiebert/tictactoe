def test_board_init():
    from tictactoe import Board 
    state = (
        (None, None, None),
        (None, None, None),
        (None, None, None),
    )
    board = Board(state)
    assert board.state == state

def test_script_output():
    import subprocess
    output = subprocess.check_output(
        ['python', 'tictactoe.py'])

    row = str((None, None, None))
    expected = '{}\n{}\n{}\n'.format(row, row, row).encode()

    assert output == expected