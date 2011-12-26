#!/usr/bin/python
from __future__ import print_function
import random
if raw_input:
    input = raw_input

rows = {'a':0, 'b':1, 'c':2}

class SpaceTakenError(Exception):
    """Indicates that a space is already played."""

def reset():
    global state
    state = []
    for _ in range(3):
        state.append([None] * 3)

def automove():
    movelist = []
    for i in range(3):
        for j in range(3):
            movelist.append((i,j))
    random.shuffle(movelist)

    moved = False
    for i, j in movelist:
        if not moved and state[i][j] is None:
            state[i][j] = 'o'
            print('The computer moved to ' + 'abc'[i] + str(j))
            moved = True

def move(move):
    if move == 'p':
        return
    row = rows[move[0]]
    col = int(move[1])
    if state[row][col] is None:
        state[row][col] = 'x'
    else:
        raise SpaceTakenError('Space has already been played.')

def winner():
    """
    Check for winning states, and return winner, or if no winner, None.
    """
    # Horizontal
    for row in state:
        if row[0] is row[1] is row[2] is not None:
            return row[0]

    # Vertical
    for col in range(3):
        if state[0][col] is state[1][col] is state[2][col] is not None:
            return state[0][col]

    # Natural Diagonal, then Reverse Diagonal
    if (state[0][0] is state[1][1] is state[2][2] is not None or
        state[0][2] is state[1][1] is state[2][0] is not None):
        return state[1][1]

def out_state():
    print('\n    0   1   2\n  +-----------+')
    for i, row in enumerate(state):
        if i is not 0:
            print('  +---+---+---+')
        to_print = ['abc'[i] + ' ']
        for space in row:
            if space:
                to_print.append(' {0} '.format(space))
            else:
                to_print.append('   ')
        to_print.append('')
        print('|'.join(to_print))
    print('  +-----------+\n')

def full():
    ret = True
    for row in state:
        for space in row:
            if not space:
                ret = False
    return ret

cont = True
while cont is True:
    reset()
    while not winner() and not full():
        out_state()
        while True:
            try:
                move(input('Enter Your Move: '))
                break
            except (IndexError, KeyError, ValueError):
                print('Invalid Move.  Move should be like a0.')
            except SpaceTakenError:
                print('That space has already been played.')
        if not winner():
            automove()
    out_state()
    if winner() is 'x':
        print('You Have Won :-)')
    elif winner() is 'o':
        print('You Have Lost :-(')
    else:
        print('Cats Game :-|')
    if input('Play Again? (Y/n) ') == 'n': # Why won't is work here in python3?
        cont = False

