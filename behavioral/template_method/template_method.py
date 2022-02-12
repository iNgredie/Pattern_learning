from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """
    Абстрактный отряд. Атрибутом класса, начинающиеся с подчеркивания
    в python являются protected
    """

    def __init__(self, speed: int) -> None:
        """
        Constructor.
        :param speed: скорость отряда
        """
        self._speed = speed

    def hit_and_run(self) -> None:
        """
        Шаблонный метод:
        """
        self._move('вперед')
        self._stop()
        self._attack()
        self._move('назад')

    @abstractmethod
    def _attack(self) -> None:
        pass

    @abstractmethod
    def _stop(self) -> None:
        pass

    def _move(self, direction: str) -> None:
        """
        Передвижение - у всех отрядов одинаковоеб в шаблон не входит
        :param direction: направление движения
        """
        self._output(f'движется {direction} со скоростью {self._speed}')

    def _output(self, message: str) -> None:
        """
        Вспомогательный метод вывода сообщений, в шаблон не входит

        :param message: выводимое сообщение
        """
        print(f'Отряд типа {self.__class__.__name__} {message}')


class Archers(Unit):
    """
    Лучники
    """
    def _attack(self) -> None:
        self._output('обстреливает врага')

    def _stop(self) -> None:
        self._output('останавливается в 100 шагах от врага')


class Cavalrymen(Unit):
    """
    Кавалеристы
    """

    def _attack(self) -> None:
        self._output('на полмном скаку врезается во вражеский строй')

    def _stop(self) -> None:
        self._output('летит вперед, не останавливаясь')


if __name__ == '__main__':
    print('OUTPUT:')
    archers = Archers(4)
    archers.hit_and_run()
    cavalrymen = Cavalrymen(8)
    cavalrymen.hit_and_run()
