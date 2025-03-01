from abc import ABC, abstractmethod


class InitLoggerMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект {class_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        BaseProduct.product_count += 1


    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def __add__(self, other):
        pass


    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, value):
        if value < 0:
            print("Цена не может быть отрицательной.")
        else:
            self._price = value


    @classmethod
    def new_product(cls, data: dict):
        return cls(**data)


class Product(InitLoggerMixin, BaseProduct):
    """Класс для продукции"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)


    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return self._price * self.quantity + other._price * other.quantity
