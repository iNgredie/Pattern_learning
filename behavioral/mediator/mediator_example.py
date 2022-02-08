import inspect
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class Colleague(ABC):
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @staticmethod
    def receive(message: str) -> None:
        pass


class Bill(Colleague):
    def send(self, message: str) -> None:
        self._mediator.send(message)

    @staticmethod
    def receive(message: str) -> None:
        print(f'Билл получил сообщение: {message}')


class Steve(Colleague):
    def send(self, message: str) -> None:
        self._mediator.send(message)

    @staticmethod
    def receive(message: str) -> None:
        print(f'Стив прочитал в скайпе сообщение: {message}')


class SkypeBetweenTwoColleagues(Mediator):
    def __init__(self) -> None:
        self._first = None
        self._second = None

    def set_first(self, first: Colleague) -> None:
        self._first = first

    def set_second(self, second: Colleague) -> None:
        self._second = second

    def send(self, message: str) -> None:
        sender = inspect.currentframe().f_back.f_locals['self']
        receiver = self._first if sender == self._second else self._second
        receiver.receive(message)


if __name__ == '__main__':
    print('OUTPUT:')
    skype = SkypeBetweenTwoColleagues()
    bill = Bill(skype)
    steve = Steve(skype)
    skype.set_first(bill)
    skype.set_second(steve)
    bill.send('Начинай работать бездельник!')
    steve.send('Нет')