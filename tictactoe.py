#!/usr/bin/python
from __future__ import print_function
import random

try:
    input = raw_input
except NameError:
    pass

rows = {'a':0, 'b':1, 'c':2}

class SpaceTakenError(Exception):
    """Indicates that a space is already played."""

def reset():
    global state
    state = []
    for _ in range(3):
        state.append([None] * 3)

def vectors():
    vectors = []
    for i in range(3):
        vectors.append(tuple([(i,j) for j in range(3)]))
        vectors.append(tuple([(j,i) for j in range(3)]))
    vectors.append(((0,0),(1,1),(2,2)))
    vectors.append(((0,2),(1,1),(2,0)))
    return vectors

def automove(level=1):
    """A multi-difficulty AI"""
    # 0 - a0, a1, ..., c2
    # 1 - random
    # 2 - blocks + random
    # 3 - fills + blocks + random
    movelist = []
    for i in range(3):
        for j in range(3):
            movelist.append((i,j))
    if level > 0:
        random.shuffle(movelist)
    if level >= 3:
        for vector in vectors():
            fills = [state[i][j] for i, j in vector]
            if fills.count('o') == 2 and fills.count(None) == 1:
                movelist = random.shuffle(list(vector))
    if level >= 2:
        for vector in vectors():
            fills = [state[i][j] for i, j in vector]
            if fills.count('x') == 2 and fills.count(None) == 1:
                movelist = random.shuffle(list(vector))
    for i, j in movelist:
        if state[i][j] is None:
            state[i][j] = 'o'
            print('The computer moved to ' + 'abc'[i] + str(j))
            return

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
    """Check for winning states, and return winner or None"""
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
    for row in state:
        for space in row:
            if not space:
                return False
    return True

while True:
    try:
        difficulty = int(input('Difficulty: (0-3) '))
        if difficulty not in range(4):
            raise ValueError
        break
    except ValueError:
        print('Invalid Difficulty.')
    except (EOFError, KeyboardInterrupt):
        raise SystemExit

while True:
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
            except (EOFError, KeyboardInterrupt):
                raise SystemExit
        if not winner():
            automove(difficulty)
    out_state()
    if winner() is 'x':
        print('You Have Won :-)')
    elif winner() is 'o':
        print('You Have Lost :-(')
    else:
        print('Cats Game :-|')
    try:
        if input('Play Again? (Y/n) ') in 'nN':
            break
    except (EOFError, KeyboardInterrupt):
        break

