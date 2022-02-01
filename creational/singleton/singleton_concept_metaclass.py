"""
Синглтон через метакласс
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументво в __init__
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любоей одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """
        pass


if __name__ == '__main__':
    first_obj = MyClass()
    second_obj = MyClass()
    print(f'Переменные сылаются на один объект: {first_obj is second_obj}')
