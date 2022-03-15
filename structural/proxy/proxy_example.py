class Imath:
    """
    Интерфейс для прокси и реального субъекта
    """

    def add(self, x: int, y: int):
        raise NotImplementedError()

    def sub(self, x: int, y: int):
        raise NotImplementedError()

    def mul(self, x: int, y: int):
        raise NotImplementedError()

    def div(self, x: int, y: int):
        raise NotImplementedError()


class Math(Imath):
    """
    Реальный субъект
    """
    def add(self, x: int, y: int):
        return x + y

    def sub(self, x: int, y: int):
        return x - y

    def mul(self, x: int, y: int):
        return x * y

    def div(self, x: int, y: int):
        return x / y


class Proxy(Imath):
    """
    Прокси
    """

    def __init__(self):
        self.math = None

    # Быстрые операции - не требуются реального субъекта
    def add(self, x: int, y: int):
        return x + y

    def sub(self, x: int, y: int):
        return x - y

    # Медленная операция - требует создания реального субъекта
    def mul(self, x: int, y: int):
        if not self.math:
            self.math = Math()
        return self.math.mul(x, y)

    def div(self, x: int, y: int):
        if y == 0:
            return float('inf')
        if not self.math:
            self.math = Math()
        return self.math.div(x, y)


if __name__ == '__main__':
    p = Proxy()
    xxx, yyy = 4, 2
    print('4 + 2 = ' + str(p.add(xxx, yyy)))
    print('4 + 2 = ' + str(p.sub(xxx, yyy)))
    print('4 + 2 = ' + str(p.mul(xxx, yyy)))
    print('4 + 2 = ' + str(p.div(xxx, yyy)))
