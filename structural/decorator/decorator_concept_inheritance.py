from abc import ABC, abstractmethod


class Component(ABC):
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Конкретные Компоненты предоставляют реализации поведения по умаолчанию Может
    быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return 'ConcreteComponent'


class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - опеределить интерфейс обертки для
    всех конкретных декоратовро. Реализация кода обертки по умолчанию может
    включать в себя поле для хранения завернутого компонента и средства его
    инициализации.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        Декоратор делегирует всю работы обернутому компонету.
        """
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Конкретные Декораторы вызывают обернутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могу вызывать родительскую реализацию операции,
        вместо того, чтобы вызвать обернутый объект напрямую. Такой подход
        упращает расширение классов декораторов.
        """
        return f'ConcreteDecoratorA({self.component.operation()})'


class ConcreteDecoratorB(Decorator):
    """
    Декораторы могут выполнять свое поведение до или после вызвова обернутого
    объекта
    """

    def operation(self) -> str:
        return f'ConcreteDecoratorB({self.component.operation()})'


def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остается незавимимым от конкретных классов компонентов, с
    которым работает.
    """
    print(f'RESULT: {component.operation()}', end='')


if __name__ == '__main__':
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    simple = ConcreteComponent()
    print('Client: I`ve got a simple component:')
    client_code(simple)
    print('\n')
    # ...так и декорированные.
    #
    # Обратите внимание, что декораторы могу обертывать не только простые
    # компоненты, но и другие декораторы.

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print('Client: Now I`ve got ad decorated component:')
    client_code(decorator2)
