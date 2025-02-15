class Product:
    """Класс для продукции"""

    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта продукта"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        Product.product_count += 1

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

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
        return cls(data["name"], data["description"], data["price"], data["quantity"])


class Category:
    """Класс для категорий"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """Инициализация объекта категории"""
        self.name = name
        self.description = description
        self._products = products if products else []
        self.product_count = len(self._products)

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product):
        """Добавляет товар в категорию и обновляет счетчики"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self._products.append(product)
        self.product_count += 1
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для получения списка товаров в формате строки"""
        return [f"{str(product)}\n" for product in self._products]



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)