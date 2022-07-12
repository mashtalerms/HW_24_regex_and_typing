from typing import Iterable

from exceptions import CommandDoesntExist
import re


"""Manipulation function"""
def build_query(cmd, val, file_list) -> Iterable:

    """Get data with filtered query"""
    if cmd == 'filter':
        if not isinstance(val, str):
            raise TypeError
        return list(filter(lambda x: val in x, file_list))

    """Get data from specified column"""
    if cmd == 'map':
        if not str(val).isdigit():
            raise ValueError
        return map(lambda x: x.split(' ')[int(val)], file_list)

    """Get unique data"""
    if cmd == 'unique':
        return list(set(file_list))

    """Get sorted data in asc or desc order"""
    if cmd == 'sort':
        if val not in ('asc', 'desc'):
            raise ValueError

        if val == 'desc':
            return list(sorted(file_list, reverse=True))
        return list(sorted(file_list, reverse=False))

    """Get limited data"""
    if cmd == 'limit':
        if not str(val).isdigit():
            raise ValueError
        return list(file_list)[:int(val)]

    """Get data from regular expression"""
    if cmd == 'regex':
        if not isinstance(val, str):
            raise TypeError
        val = '+'.join(val.split(' '))         # Replacing space (space comes from '+' from args) to '+'
        return [line for line in file_list if re.findall(re.compile(val, re.IGNORECASE), line)]

    """If inputed command doest exist"""
    raise CommandDoesntExist
