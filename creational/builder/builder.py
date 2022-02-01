"""
Паттерн Строитель актуален только тогда, когда ваши продукты
достаточно сложны, состоят из многих частей и требуют общирной конфигурации.

Основное отличие паттерна Builder от други порождающих паттерно - то, что различные
конкретные строители могут создавать несвязные друг с другом продукты.
По простому - различные строители не обязаны следовать одному общему интерфейсу.
"""
from abc import ABC, abstractmethod


class Product:
    """Некоторый слоный объект, который состоит из множества частей"""

    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Продукт состоит из: {", ".join(self.parts)}')


class Builder(ABC):
    """
    Интерфейс строителя объявляет создающие методы для различных частей продукта
    """
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def create_part_a(self) -> None:
        pass

    @abstractmethod
    def create_part_b(self) -> None:
        pass

    @abstractmethod
    def create_part_c(self) -> None:
        pass


class ConcreteBuilder(Builder):
    """
    Классы конкретных строитеелей следуют интерфейсу строителя и предоставляют
    конкретные реализации шагов построения.
    В программе может быть несоклько строителей, реализованных по-разному.
    """
    _product: Product

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой обхект продукта,
        который используется в дальнешей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        """
        Конкретные Строители должны предоставить свои собственные методы
        получения результатов. Это связано с тем, что различные типы строителей
        могу создавать совершенно разные прлдукты с разными интерфейсами.

        Как правило, после возвращения конечного результата клиенту, экзепляр
        строителя должен быть готов к началу производства следующего продукта.
        Поэтому обычной практикой является вызов метода сброса в конце тела
        метода get_product. Однако такое поведение не является обязательым, вы
        можете заставить своих строителей ждать явного запроса на сброс из кода
        клиента, прежде чем избавиться от предыдущего результата.
        """
        product = self._product
        self.reset()
        return product

    def create_part_a(self) -> None:
        self._product.add('Часть A')

    def create_part_b(self) -> None:
        self._product.add('Часть B')

    def create_part_c(self) -> None:
        self._product.add('Часть C')


class Director:
    """
    Директор отвечает только за выполнение шагов построения в определенной
    последовательности. Это полезно при производстве продуктов в определенном
    порядке или особой конфигурации. Строго говоря, класс Директо необязателен,
    так как клиент может напрямую управлять строителями.
    """
    builder: Builder

    def __init__(self, builder) -> None:
        self.builder = builder

    def builder_minimal_viable_product(self) -> None:
        self.builder.create_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.create_part_a()
        self.builder.create_part_b()
        self.builder.create_part_c()


if __name__ == '__main__':
    """
    Клиентский код создает объект-строитель, передает его директору, а затем
    инициирует процесс постороения. Конечный результать извлекается из объекта-
    стриотеля.
    """
    c_builder = ConcreteBuilder()
    director = Director(c_builder)
    print('Базовая комплектация продукта: ')
    director.build_full_featured_product()
    c_builder.product.list_parts()

    print('\n')

    print('Полная комплектация продукта: ')
    director.build_full_featured_product()
    c_builder.product.list_parts()

    print('\n')

    # Помните, что паттерн Строитель можно использовать без класса Директор.
    print('Создаем продукт без директора: ')
    c_builder.create_part_a()
    c_builder.create_part_b()
    c_builder.product.list_parts()

