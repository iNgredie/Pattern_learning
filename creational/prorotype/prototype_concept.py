import copy


class Prototype:
    """
    Класс прототипа, который будет хранить все зарегестрированные прототиы
    и делать их копии
    """
    _objects: dict

    def __init__(self):
        self._objects = {}

    def register(self, name, new_prototype):
        """
        Регистрируем новый прототип, чтобы потом его копировать
        """
        self._objects[name] = new_prototype

    def unregister(self, name):
        """
        Удаляем зарегистрированный прототип
        """

    def clone(self, name, **new_attr):
        """
        Клонирование прототипа с возможностью переопределения атрибутов
        """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(new_attr)
        return obj


class CircularReference:
    """
    Класс, объекто которого будет имитировать механгизх циклических ссылок
    """
    link: 'Component'

    def set_link(self, component: 'Component'):
        self.link = component


class Component:
    """
    Класс, который содержит артирбуты с изменянемыми и неизменными типами данных
    """

    def __init__(self, immutable, mutable, circular_reference):
        """
        В Python неизменяемые значения предеаются по значению, а изменяемы по ссылке
        Объект некоторого другого класса также передает по ссылке, так что его можно
        считать mutable
        :param immutable: параметр неизменяемого типа данных
        :param mutable: параметр изменяемого типа данных
        :param circular_reference: параметр, который будет сожержать цикличыескую ссылку
        """
        self.immutable = immutable
        self.mutable = mutable
        self.circular_reference = circular_reference

    # Если хотим переопределить механизм поверхностного копирования
    # def __copy__(self):
    #     pass

    # Если хотим переопределить механизм глубого копирования
    # def __deepcopy__(self):
    #     pass


if __name__ == '__main__':
    prototype_obj = Prototype()

    mutable_data = [1, 2, 3, {'a': 2}]
    circular_ref = CircularReference()
    component_obj = Component('immutable', mutable_data, circular_ref)

    prototype_obj.register('obj', component_obj)
    clone_obj = prototype_obj.clone('obj')

    if clone_obj is not clone_obj:
        print('клонирование прошло успешно')

    print(f'Исходный объект ({id(component_obj):X}): {vars(component_obj)}')
    print(f'Объект-клон ({id(clone_obj):X}): {vars(clone_obj)}')
