from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """
    Интерфейс Стратегии Объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определенного
    Конкретными Стратегиями.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data, reverse=True)


class Context:
    """
    Контекст определяет интерфейс, представялющий интерес для клиентов
    """
    def __init__(self, strategy: Strategy) -> None:
        """
        Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для ее изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Обычно Конекст позволяет заменить объект Стратегии во время выполнения.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Обычно Контекст позволяет заменить объект Стратегии во время выполнения.
        """

        self._strategy = strategy


    def do_some_business_logic(self) -> None:
        """
        Вместо того, чтобы самостоятельно реализовывать множественные версии
        алгоритма, Контекст делегирует некоторую работу объекту Стратегии.
        """
        print('Context: Sorting data using the strategy (not sure how it`ll do it)')
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(', '.join(result))


if __name__ == '__main__':
    print('Client: Strategy is set to normal sorting.')
    context = Context(ConcreteStrategyA())
    context.do_some_business_logic()
    print()
    print('Client: Strategy is set to reverse sorting.')
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
