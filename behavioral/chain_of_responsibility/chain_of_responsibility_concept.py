from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод цепочки обработчиков. Он
    также объявляет метод для выполения запроса.
    """

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базовго класса
    обработчика.
    """
    _next_handler: Handler = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # спобом, вот так:
        # monkey.set_next(squirrel).set_next(di)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)


"""
Все Конктретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Banana':
            return f'Monkey: I`ll eat the {request}'
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Nut':
            return f'Squirrel: I`ll eat the {request}'
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'MeatBall':
            return f'Dog I`ll eat the {request}'
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    """

    for food in ['Nut', 'Banana', 'Cup of coffee']:
        print(f'\nClient: Who wants a {food}?')
        result = handler.handle(food)
        if result:
            print(f'  {result}', end='')
        else:
            print(f'  {food} was left untouched.', end='')


if __name__ == '__main__':
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # Клиент должен имтеь возможность отпавлять запрос любому обработчику, а не
    # только первому в цепочке.

    print('Chain: Monkey > Squirrel > Dog')
    client_code(monkey)
    print('\n')

    print('Subchain: Squirrel > Dog')
    client_code(squirrel)
