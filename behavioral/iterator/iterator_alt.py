"""
Implementation of the iterator pattern using the iterator protocol from Python
*TL;DR
Traverses a container and accesses the container's elements.
"""
from __future__ import annotations


class NumberWords:
    """
    Count by word number, up to a maximum of five
    """

    _WORD_MAP = (
        'one',
        'two',
        'three',
        'four',
        'five',
    )

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> NumberWords: # this makes the class an Iterable
        return self

    def __next__(self) -> str: # this makes the class an Iterator
        if self.start > self.stop or self.start > len(self._WORD_MAP):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


if __name__ == '__main__':

    for number in NumberWords(start=1, stop=2):
        print(number)

    print('-----------')

    for number in NumberWords(start=1, stop=5):
        print(number)
