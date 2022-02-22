from abc import ABC, abstractmethod


class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int):
        pass


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f'DrawingAPI1.circle at {x}:{y} radius {radius}')


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f'DrawingAPI2.circle at {x}:{y} radius {radius}')


class Shape:
    def draw(self):
        pass

    def resize_by_percentage(self, pct):
        pass


class CircleShape(Shape):
    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        drawing_api: DrawingAPI,
    ):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__drawing_api = drawing_api

    def draw(self):
        self.__drawing_api.draw_circle(self.__x, self.__y, self.__radius)

    def resize_by_val(self, val):
        self.__radius *= val


if __name__ == '__main__':
    circle_from_a1 = CircleShape(1, 2, 3, DrawingAPI1())
    circle_from_a1.draw()

    circle_from_a2 = CircleShape(5, 7, 11, DrawingAPI2())
    circle_from_a2.resize_by_val(2)
    circle_from_a2.draw()
