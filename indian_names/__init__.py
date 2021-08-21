"""
As simple as the name goes.
The module generates random names of Indian origin.
"""

from os.path import abspath, join, dirname
from typing import Dict, Literal
import random


__title__ = 'indian_names'
__version__ = '0.2'
__author__ = 'ByteBaker'
__license__ = 'BSD 3-Clause License'


def _path_to(file: str):
    return abspath(join(dirname(__file__), file))


FILES: Dict[str, str] = {
    'first:male': _path_to('first.male.names'),
    'first:female': _path_to('first.female.names'),
    'last': _path_to('last.names')
}


def _get_name(filename: str) -> str:
    """
    Function returns a random name (first or last)
    from the filename given as the argument.

    Internal function. Not to be imported.
    """

    LINE_WIDTH: int = 20 + 1    # 1 for \n

    with open(filename) as names:
        try:
            total_names = int(next(names))
            nth_name_to_read: int = random.randint(1, total_names)

            # Here 'nth_name_to_read' lines are skipped that include
            # the first line (with no of lines) and n-1 names
            # Next read would always be the desired name
            bytes_to_seek: int = LINE_WIDTH * nth_name_to_read

            _ = names.seek(bytes_to_seek)   # Now skipped n - 1 names

            name: str = next(names).strip()
            return name

        except StopIteration:
            # Return empty string if the file is empty
            return ''


def get_first_name(gender: Literal['male', 'female'] = None) -> str:
    """
    Generate a random first name for the 'gender' given.
    """
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        errmsg = f"Invalid value '{gender}'. Only 'male' & 'female' supported for 'gender'"
        raise ValueError(errmsg)

    return _get_name(FILES[f'first:{gender}']).title()


def get_last_name() -> str:
    """
    Generate a random last name.
    """
    return _get_name(FILES['last']).title()


def get_full_name(gender: Literal['male', 'female'] = None) -> str:
    """
    Generate a random full name for the 'gender' given.
    """
    # Getting first name before last saves wasting
    # a read operation if 'gender' value is invalid
    first_name = get_first_name(gender)
    last_name = get_last_name()

    # Make sure last name and first name aren't the same (e.g. Kumar Kumar)
    while first_name == last_name:
        first_name = get_first_name(gender)

    return f'{first_name} {last_name}'


__all__ = [
    'get_first_name',
    'get_last_name',
    'get_full_name'
]