from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Абстрактный класс, который описывает интерфейся для продуктов некоторого семейства.
    Каждый продукт этого семейсвта должен реализовать этот интерфейс.
    """

    @abstractmethod
    def a_function(self) -> str:
        """
        Некоторый фунционал, который должны реализовать всеп продукты
        """
        pass


class ProductA1(AbstractProductA):
    def a_function(self) -> str:
        return 'Результат работы продукта A1'


class ProductA2(AbstractProductA):
    def a_function(self) -> str:
        return 'Результат работы продукта A2'


class AbstractProductB(ABC):
    """
    Абстрактный класс, который описывает интерфейс для другого семейства продуктов.
    Каждый продукт этого семейства должен реализовать этот интерфейс.
    """
    @abstractmethod
    def b_function(self) -> None:
        """
        У продукта B есть свой некоторый ползеный функционал
        """
        pass

    @abstractmethod
    def b_collaborate_with_a(self, collaborator: AbstractProductA) -> None:
        """
        Также продукт B можете взаимодействовать с продуктами A той же вариации,
        например B1-A1, B2-A2 и тд.
        """
        pass


class ProductB1(AbstractProductB):
    def b_function(self) -> str:
        return 'Результат работы продукта B1'

    def b_collaborate_with_a(self, collaborator: AbstractProductA) -> str:
        """
        Продукт B1 корректно работает только с продуктом A1.
        Но он может принимать объект любого наследника асбтрактного
        класса AbstractProductA в качестве аргумента
        """
        result = collaborator.a_function()
        return f'Результат совместной работы B1 с объектом AbstractProductA ({result})'


class ProductB2(AbstractProductB):
    def b_function(self) -> str:
        return 'Результат работы продукта B2'

    def b_collaborate_with_a(self, collaborator: AbstractProductA) -> str:
        """
        Продукт B2 коректно работает только с продуктом A2.
        Но он может принимать объект любого наследника асбтрактного
        класса AbstractProductA в качестве аргумента
        """
        result = collaborator.a_function()
        return f'Результат совместной работы B2 с объектом AbstractProductB ({result})'


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной фабрики объявляет набор методов, которые возвращают
    различные асбтрактные продукты. Эти продукты назаываются семейством и связяны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимойдействовать моежду собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass


    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class Factory1(AbstractFactory):
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


class Factory2(AbstractFactory):
    """
    Каждый Конктретная Фабрика имеет соответствующую вариацию продукта.
    """
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


def client_code(factory: AbstractFactory) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Асбтрактная Фабрика и Абстрактный Продукт. Это позволяет предавать
    любой подкласс фабрики или прдукта клиетскому коду, не нарушая его.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_b.b_function()}')
    print(f'{product_b.b_collaborate_with_a(product_a)}')


if __name__ == '__main__':
    print('Client: тестируем клиентский код с первой фабрикой:')
    client_code(Factory1())
    print('\n')
    print('Client: тестируем клиентский код со второй фабрикой:')
    client_code(Factory2())
