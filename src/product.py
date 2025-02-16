class Product:
    """Класс для продукции"""

    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Цена не может быть отрицательной.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict):
        return cls(**data)
