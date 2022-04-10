"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator
*TL;DR
Traverses a container and accesses the container's elements.
"""
from typing import Generator


def count_to(count):
    """
    Counts by word numbers, up to a maximum of five
    """
    numbers = ['one', 'two', 'three', 'four', 'five']
    yield from numbers[:count]


# Test the generator
def count_to_two() -> Generator:
    return count_to(2)


def count_to_five() -> Generator:
    return count_to(5)


if __name__ == '__main__':

    for number in count_to_two():
        print(number)

    print('----------------')

    for number in count_to_five():
        print(number)
