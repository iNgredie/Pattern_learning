from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соотвестствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Раеадизации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation(self) -> str:
        return 'ConcreteImplementationA: результат работы платформы A'


class ConcreteImplementationB(Implementation):
    def operation(self) -> str:
        return 'ConcreteImplementationB: результат работы платформы B'


class Abstraction:
    """
    Абстракция устанавливает интерфейс для `управляющей` части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настояющую работу.
    """

    def __init__(self, impl: Implementation) -> None:
        self.impl = impl

    def operation(self) -> str:
        return (
            f'ExtendedAbstraction: Extended operation with:\n'
            f'{self.impl.operation()}'
        )


class ExtendedAbstraction(Abstraction):
    """
    Можно расширить Асбтракцию без изменения классов Реализации.
    """

    def operation(self) -> str:
        return (
            f'ExtendedAbstraction: Extended operation with:\n'
            f'{self.impl.operation()}'
        )


def client_code(abstract: Abstraction) -> None:
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определенным объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.
    """
    print(abstract.operation(), end='')


if __name__ == '__main__':
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print('\n')

    implementation = ConcreteImplementationB()
    abstraction = Abstraction(implementation)
    client_code(abstraction)
