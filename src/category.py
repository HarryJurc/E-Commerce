from src.product import Product


class Category:
    """Класс для категорий"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """Инициализация объекта категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.product_count = len(self.__products)

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Добавляет товар в категорию и обновляет счетчики"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)
        self.product_count += 1
        Category.product_count += 1

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        """Геттер для получения списка товаров в формате строки"""
        return [f"{str(product)}\n" for product in self.__products]
