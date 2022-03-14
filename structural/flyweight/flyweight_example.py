class Lamp:
    def __init__(self, color: str):
        self.color = color


class LampFactory:
    lamps = {}

    @staticmethod
    def get_lamp(color: str) -> Lamp:
        return LampFactory.lamps.setdefault(color, Lamp(color))


class TreeBranch:
    def __init__(self, branch_number: int):
        self.branch_number = branch_number

    def hang(self, lamp: Lamp):
        print(f'Hang {lamp.color}[{id(lamp)}] lamp on'
              f'branch {self.branch_number} [{id(self)}]')


class ChristmasTree:
    def __init__(self):
        self.lamps_hung = 0
        self.branches = {}

    def get_branch(self, number: int):
        return self.branches.setdefault(number, TreeBranch(number))

    def dress_up_the_tree(self):
        for i in range(3):
            self.hand_lamp('red', i)
            self.hand_lamp('blue', i)
            self.hand_lamp('yellow', i)

    def hand_lamp(self, color: str, branch_number: int):
        self.get_branch(branch_number).hang(LampFactory.get_lamp(color))
        self.lamps_hung += 1


if __name__ == '__main__':
    ChristmasTree().dress_up_the_tree()
