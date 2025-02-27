from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов, наследуется от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        model: str,
        efficiency: float,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.efficiency = efficiency
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}), {self.color}, {self.memory}GB, "
            f"{self.price} руб. Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного типа продукта")
        return super().__add__(other)
