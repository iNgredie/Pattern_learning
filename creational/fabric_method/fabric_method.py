from abc import ABC, abstractmethod


class Product(ABC):
    """
    Абстрактный класс, который описывает интерфейс для продуктов.
    Каждый продукт должен реализовать данный интерфейс.
    """
    @abstractmethod
    def operation(self) -> str:
        pass


class ProductA(Product):
    def operation(self) -> str:
        return 'операция для продукта A'


class ProductB(Product):
    def operation(self) -> str:
        return 'операция для продукта B'


class Creator(ABC):
    """
    Класс Creator объявлет фабричный метод, который должен возвращать объект
    класса Product. Подклассы создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def factory_method(self) -> Product:
        """
        Обратите внимание, что Creator может также обеспечить реализацию
        фабричного метода по умолчанию
        """
        pass

    def some_operation(self) -> str:
        """
        Несмотря на название, оснаваная обязанность Создателя не заключается в
        создание продуктов. Обычно он содержит некоторую базовую бизнес-логику,
        которая основана на объектах продуктов, вовзращаемых фабричным методом.
        Подклассы могут косвенно изменять эту бизнес-логику, переопределяя
        фабричный метод и возвращая из него другой тип продукта.
        """
        # Вызываем фабричный метод, чтобы получить объект продукта.
        product = self.factory_method()
        # Далее, работаем с этим продуктом.
        result = f'Creator: результат операции - {product.operation()}'

        return result


class CreatorA(Creator):
    """
    Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
    результирующего продукта в базовом классе.

    Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактоного продукта, хотя фактически из метода возвращается кокретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретный
    классов продуктов
    """

    def factory_method(self) -> Product:
        return ProductA()


class CreatorB(Creator):
    def factory_method(self) -> Product:
        return ProductB()


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конктретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать  с создателем через
    базовый интерфейс, выф можеете передать ему любой подкласс создателя.
    """
    print(f'{creator.some_operation()}')


if __name__ == '__main__':
    print('App: запуск с CreatorA:')
    client_code(CreatorA())
    print('\n')
    print('App: запуск с CreatorB:')
    client_code(CreatorB())
