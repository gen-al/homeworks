# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1,16))
    field.append(EMPTY_MARK)
    random.shuffle(field)
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, len(field)-1, 4):
        print(field[i: i + 4])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    ideal_field = list(range(1,15))
    ideal_field.append(EMPTY_MARK)
    return ideal_field == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    if field.index(EMPTY_MARK) < 4 and key == 'w':
        raise IndexError('You do not can go up!')
    elif field.index(EMPTY_MARK) > 11 and key == 's':
        raise IndexError('You do not can go down!')
    elif field.index(EMPTY_MARK) % 4 == 0 and key == 'a':
        raise IndexError('You do not can go left!')
    elif (field.index(EMPTY_MARK) - 3) % 4 == 0 and key == 'd':
        raise IndexError('You do not can go right!')

    
    field.insert(field.index(EMPTY_MARK) + MOVES[key],field.pop(field.index(EMPTY_MARK)))
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        input_user = input('Press w a s d for your turn. >>> ')
        if input_user.lower() in 'wasd':
            return input_user.lower()


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    
    field = shuffle_field()

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field,move)
        except IndexError as e:
            print(e)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()