"""
Продукт определяет общий интерфейс объектов,
которые может произвести создатель и его подклассы
"""
from abc import ABC, abstractmethod

"""
Конкретные продукты сожержат код различных продуктов. Продукты
будут отличаться реализацией, но интерфейс у них будет общий.
"""

"""
Создатель объявляет фабричный метод, который должен возвращать
новые объекты продуктов. Важно, чтобы тип результата совпадал с 
общим интерфейсом продуктов.

Зачастую фабричный метод объеявляет абстрактным, чтобы заставить
все подклассы реализовать его по-своему. Но он может возвращать и некий
стандартный продукт.

Несмотря на название, важно понимать, что создание продуктов не является
единственной функцией создателя. Обычно он содержит и другой полезный
код работы с продуктом. Аналогия: большая софтверная компания может иметь
центр подготовки программистов, но основная задача компании - создавать
программные продукты, а не готовить программистов.
"""

"""
Конкретные создатели по-своему реализуют фабричный метод, производя те или
иные конкретные продукты.

Фабричный метод не обязан все время создавать новые объекты. Его можно
переписать так, чтобы возвращать существующие объекты из какого-то хранилища
кэша.
"""


class User(ABC):
    """
    Абстрактный пользователь
    """
    pass


class MtsUser(User):
    """
    Пользователь МТС, с номером телефона.
    """

    def __init__(self, phone: str):
        print(f'Created MtsUser: {phone}')


class LiteboxUser(User):
    """
    Пользователь Лайтбокс, с почтовым ящиком
    """

    def __init__(self, email: str):
        print(f'Created LiteboxUser {email}')


class Credentials(ABC):
    """
    Абстрактные учетные данные
    """

    pass


class LiteboxCredentials(Credentials):
    """
    Учетные данные для входа в Лайтбокс
    """

    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password


class MtsCredentials(Credentials):
    """
    Учетные данные для всхода в МТС
    """

    def __init__(self, phone: str, password: str):
        self._phone = phone
        self._password = password

    @property
    def phone(self):
        return self._phone

    @property
    def password(self):
        return self._password


class Authenticator(ABC):
    """
    Абстрактный аутентификатор
    """

    @abstractmethod
    def authenticate(self, credentials: Credentials) -> User:
        pass


class LiteboxAuthenticator(Authenticator):
    """
    Аутентификатор Лайтбокс
    """

    def authenticate(self, credentials: LiteboxCredentials) -> LiteboxUser:
        print(f'Authenticate by email: {credentials.email}')
        return LiteboxUser(credentials.email)


class MtsAuthenticator(Authenticator):
    """
    Аутентификатор МТС
    """

    def authenticate(self, credentials: MtsCredentials) -> MtsUser:
        print(f'Authenticate by phone {credentials.phone}')
        return MtsUser(credentials.phone)


def authenticate(authenticator: Authenticator, credentials: Credentials) -> User:
    return authenticator().authenticate(credentials)


if __name__ == '__main__':
    # Форма логина МТС (phone + password)
    phone = '+79876543210'
    password = '****'
    credentials = MtsCredentials(phone, password)
    user: MtsUser = authenticate(MtsAuthenticator, credentials)

    print('==========================================')

    # Форма логина Лайтбокс (email + password)
    email = 'litebox@litebox.ru'
    password = '****'
    credentials = LiteboxCredentials(email, password)
    user: LiteboxUser = authenticate(LiteboxAuthenticator, credentials)