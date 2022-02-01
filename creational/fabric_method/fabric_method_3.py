from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ProductA(Product):
    def operation(self) -> str:
        return 'Результат операции для продукта A'


class ProductB(Product):
    def operation(self) -> str:
        return 'Резульать операции для продукта B'


class Creator:
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        return f'Creator: результат операции - {product.operation()}'


class CreatorA(Creator):
    def factory_method(self) -> Product:
        return ProductA()


class CreatorB(Creator):
    def factory_method(self) -> Product:
        return ProductB()


def client_code(creator: Creator) -> None:
    print(f'{creator.some_operation()}')


if __name__ == '__main__':
    print('App: запуск с CreatorA')
    client_code(CreatorA())
    print('\n')
    print('App: запуск с CreatorB')
    client_code(CreatorB())

