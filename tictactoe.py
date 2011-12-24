#!/usr/bin/python
from __future__ import print_function
import sys
if sys.version_info[0] < 3:
    input = raw_input

# Initialize Game State
# False = Computer, True = User
state = {}
rows = 'a','b','c'
columns = '0','1','2'

def reset():
    for x in rows:
        state[x] = {}
        for y in columns:
            state[x][y] = None

def automove():
    moved = False
    for key in state:
        for subkey in state[key]:
            if not moved and state[key][subkey] is None:
                state[key][subkey] = 'o'
                print('The computer moved to ' + key + subkey)
                moved = True

def move(move):
    if state[move[0]][move[1]] is None:
        state[move[0]][move[1]] = 'x'
    else:
        raise ValueError('Space has already been played')

def winner():
    """
    Check for winning states, and return winner, or if no winner, None.
    """
    # Horizontal
    for row in state:
        a,b,c = columns
        if state[row][a] is state[row][b] is state[row][c] is not None:
            return state[row][a]

    # Vertical
    for col in columns:
        a,b,c = rows
        if state[a][col] is state[b][col] is state[c][col] is not None:
            return state[a][col]

    # Natural Diagonal, then Reverse Diagonal
    r = rows
    c = columns
    if state[r[0]][c[0]] is state[r[1]][c[1]] is state[r[2]][c[2]] is not None:
        return state[r[0]][c[0]]
    if state[r[0]][c[2]] is state[r[1]][c[1]] is state[r[2]][c[0]] is not None:
        return state[r[0]][c[2]]

def out_state():
    print('\n    {0}   {1}   {2}\n  +-----------+'.format(state['a'].keys()[0],
                                                          state['a'].keys()[1],
                                                          state['a'].keys()[2]))
    for row in state:
        if row is not state.keys()[0]:
            print('  +---+---+---+')
        to_print = [row + ' ']
        for space in state[row]:
            space = state[row][space]
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
        for col in state[row]:
            if not state[row][col]:
                ret = False
    return ret

cont = True
while cont is True:
    reset()
    while not winner() and not full():
        out_state()
        move(input('Enter Your Move: '))
        if not winner():
            automove()
    out_state()
    if winner() is 'x':
        print('You Have Won :-)')
    elif winner() is 'o':
        print('You Have Lost :-(')
    else:
        print('Cats Game :-|')
    if input('Play Again? (Y/n) ') is 'n':
        cont = False

