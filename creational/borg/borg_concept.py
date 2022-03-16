"""
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.
*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.
*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections:

https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

*References:
- https://fkromer.github.io/python-pattern-references/design/#singleton
- https://learning.oreilly.com/library/view/python-cookbook/0596001673/ch05s23.html
- http://www.aleax.it/5ep.html

*TL;DR
Provides singleton-like behavior sharing state between instances.
"""
from typing import Dict


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):

    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, 'state'):
                self.state = 'Init'

    def __str__(self):
        return self.state


if __name__ == "__main__":
    rm1 = YourBorg()
    rm2 = YourBorg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    assert str(rm1) == 'Running'
    assert str(rm2) == 'Running'

    rm2.state = 'Zombie'
    
    assert str(rm1) == 'Zombie'
    assert str(rm2) == 'Zombie'

    assert rm1 is not rm2

    rm3 = YourBorg()
    assert str(rm3) == 'Zombie'

    rm4 = YourBorg('Running')

    assert str(rm3) == 'Running'
