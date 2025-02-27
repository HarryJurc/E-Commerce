from src.product import Product


class LawnGrass(Product):
    """Класс для травы газонной, наследуется от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.country}, "
            f"Прорастание: {self.germination_period}, "
            f"{self.price} руб. Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного типа продукта")
        return super().__add__(other)
