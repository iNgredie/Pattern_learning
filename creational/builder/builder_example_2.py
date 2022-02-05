from abc import ABC, abstractmethod
from enum import Enum


class Cutlery(Enum):
    ...


class Product(ABC):
    """
    Продукт - создаваемый объект. Продукты, сделанные разными
    строителями, не обязаны иметь общий интерфейс.
    """
    @property
    @abstractmethod
    def name(self):
        pass


class Sushi(Product):
    @property
    def name(self) -> str:
        return 'Суши'


class Burger(Product):
    @property
    def name(self) -> str:
        return 'Бургер'


class OrderBuilder(ABC):
    """
    Интерфейс строителя объявляет шаги конструирования продуктов,
    общие для всех видов строителей
    """
    @abstractmethod
    def serve(self):
        pass

    @abstractmethod
    def pack(self):
        pass

    @abstractmethod
    def add_cutlery(self, cutlery: Cutlery):
        pass

    @abstractmethod
    def add_topings(self):
        pass

    @abstractmethod
    def add_gloves(self):
        pass

    @abstractmethod
    def get_ready_order(self) -> Product:
        pass


class SushiCutlery(Cutlery):
    FORK = 'Вилка'
    STICK = 'Палочки'


class SushiOrderBuilder(OrderBuilder):
    """
    Конкретные строители реализуют строительные шаги, каждый по-своему.
    Конкретные строители могут производить разнородные объекты,
    не имеющие общего интерфейса.
    """

    def serve(self):
        print('Крутим роллы, режем лосося')

    def pack(self):
        print('Упаковывем суши в пластиковый контейнер')

    def add_cutlery(self, cutlery: SushiCutlery):
        if cutlery == SushiCutlery.FORK:
            print('Кладем вилки')
        if cutlery == SushiCutlery.STICK:
            print('Кладем палочки')

    def add_topings(self):
        print('Кладем емкость с соевым соусом')

    def add_gloves(self):
        pass

    def get_ready_order(self) -> Product:
        return Sushi()


class BurgerOderBuilder(OrderBuilder):
    """
    Конкретный билдер
    """

    def serve(self):
        print('Печем булки, жарим котлеты')

    def pack(self):
        print('Оборачиваем бургер в бумагу')

    def add_cutlery(self, cutlery: Cutlery):
        pass

    def add_topings(self):
        print('Добавляем вторую котлету')

    def add_gloves(self):
        print('Кладем перчатки')

    def get_ready_order(self) -> Product:
        return Burger()


class Packer:
    """
    Директор определяет порядко вызова строительных шагов для
    производства той или иной конфигурации продуктов.
    """

    def __init__(self, order_builder: OrderBuilder):
        self.order_builder = order_builder

    def pack_sushi(self, cutlery: SushiCutlery):
        self.order_builder.serve()
        self.order_builder.add_topings()
        self.order_builder.add_cutlery(cutlery)
        self.order_builder.pack()
        return self.order_builder.get_ready_order()

    def pack_burger(self):
        self.order_builder.serve()
        self.order_builder.add_topings()
        self.order_builder.add_gloves()
        self.order_builder.pack()
        return self.order_builder.get_ready_order()


if __name__ == '__main__':
    """
    Обычно Клиент подает в конструктор директора уже готовый
    объект-строитель, и в дальнейшем данный директор использует
    только его. Но возможет и другой вариант, когда клиент
    передает строителя через параметр строительного метода директора.
    В этом случае можно каждый раз применять разных стриотелей для
    производства различных представлений объекта.
    """

    print('Клиент заказал Суши:')
    packer = Packer(SushiOrderBuilder())
    order = packer.pack_sushi(SushiCutlery.STICK)
    print(f'Заказ с {order.name} готов')

    print('Клиент заказал Бургер')
    packer = Packer(BurgerOderBuilder())
    order = packer.pack_burger()
    print(f'Заказ с {order.name} готов')

