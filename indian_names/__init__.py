"""
As simple as the name goes.
The module generates random names of Indian origin.
"""

from os.path import abspath, join, dirname
from typing import Dict, Literal
import random


__title__ = 'indian_names'
__version__ = '0.1'
__author__ = 'ByteBaker'
__license__ = 'BSD 3-Clause License'


def _path_to(file):
    return abspath(join(dirname(__file__), file))


FILES: Dict[str, str] = {
    'first:male': _path_to('first.male.names'),
    'first:female': _path_to('first.female.names'),
    'last': _path_to('last.names')
}


def _get_name(filename: str):
    """
    Function returns a random name (first or last)
    from the filename given as the argument.

    Internal function. Not to be imported.
    """

    # Write proper logic here.
    with open(filename) as names:
        try:
            total_names = int(next(names))
            lines_to_skip = random.randint(1, total_names)

            # Skip 'lines_to_skip'
            for _ in range(1, lines_to_skip):
                names.readline()
            
            # Last name that remains after 'skip_lines'
            name, _ = next(names).split()
            return name

        except StopIteration:
            # Return empty string if the file is empty
            return ''


def get_first_name(gender: Literal['male', 'female'] = None):
    """
    Generate a random first name for the 'gender' given.
    """
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        errmsg = f"Invalid value '{gender}'. Only 'male' & 'female' supported for 'gender'"
        raise TypeError(errmsg)

    return _get_name(FILES[f'first:{gender}']).title()


def get_last_name():
    """
    Generate a random last name.
    """
    return _get_name(FILES['last']).title()


def get_full_name(gender: Literal['male', 'female'] = None):
    """
    Generate a random full name for the 'gender' given.
    """

    last_name = get_last_name()
    first_name = get_first_name(gender)

    # Make sure last name and first name aren't the same (e.g. Kumar Kumar)
    while first_name == last_name:
        first_name = get_first_name(gender)

    return f'{first_name} {last_name}'


__all__ = [
    'get_first_name',
    'get_last_name',
    'get_full_name'
]