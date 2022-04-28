""""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves
*TL;DR
Allows object composition to achieve the same code reuse as inheritance.
"""

from __future__ import annotations

from typing import Any, Callable


class Delegator:

    def __init__(self, delegate: Delegate):
        self.delegate = delegate

    def __getattr__(self, name: str) -> Any | Callable:
        attr = getattr(self.delegate, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)

        return wrapper


class Delegate:
    def __init__(self):
        self.p1 = 123

    def do_something(self, something: str) -> str:
        return f'Doing {something}'


if __name__ == '__main__':
    delegator = Delegator(Delegate())
    assert delegator.p1 == 123

    assert delegator.do_something('nothing') == 'Doing nothing'
