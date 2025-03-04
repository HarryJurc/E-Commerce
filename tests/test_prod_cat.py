import pytest
from src.product import Product, BaseProduct
from src.category import Category


@pytest.fixture
def reset_counts():
    """Сбрасывает глобальные счетчики перед каждым тестом"""
    Product.product_count = 0
    Category.category_count = 0
    Category.product_count = 0
    BaseProduct.product_count = 0


@pytest.fixture
def sample_products():
    """Создает примеры продуктов для тестов"""
    p1 = Product("Product1", "Description1", 100.0, 10)
    p2 = Product("Product2", "Description2", 200.0, 20)
    return [p1, p2]


def test_category_creation(reset_counts, sample_products):
    category = Category("Category1", "Description1", sample_products)
    assert category.name == "Category1"
    assert category.description == "Description1"
    assert len(category.products) == 2
    assert category.product_count == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product(reset_counts, sample_products):
    category = Category("Category1", "Description1", sample_products)
    p3 = Product("Product3", "Description3", 300.0, 30)
    category.add_product(p3)
    assert len(category.products) == 3
    assert category.product_count == 3
    assert Category.product_count == 3


def test_add_product_invalid_type(reset_counts, sample_products):
    category = Category("Category1", "Description1", sample_products)
    with pytest.raises(TypeError):
        category.add_product("InvalidProduct")


def test_price_getter_and_setter(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    p1.price = 150.0
    assert p1.price == 150.0
    p1.price = -50.0
    assert p1.price == 150.0


def test_price_getter(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    assert p1.price == 100.0


def test_product_creation_invalid_price(reset_counts, capsys):
    p1 = Product("InvalidProduct", "Description", 100.0, 10)
    p1.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не может быть отрицательной." in captured.out
    assert p1.price == 100.0


def test_products_property_formatting(reset_counts, sample_products):
    category = Category("Category1", "Description1", sample_products)
    products = category.products
    assert products == ["Product1, 100.0 руб. Остаток: 10 шт.\n", "Product2, 200.0 руб. Остаток: 20 шт.\n"]


def test_price_setter_invalid_value(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    p1.price = -10.0
    assert p1.price == 100.0


def test_add_multiple_products(reset_counts):
    category = Category("Category1", "Description1")
    p1 = Product("Product1", "Description1", 100.0, 10)
    p2 = Product("Product2", "Description2", 200.0, 20)
    p3 = Product("Product3", "Description3", 300.0, 30)
    category.add_product(p1)
    category.add_product(p2)
    category.add_product(p3)

    assert len(category.products) == 3
    assert category.product_count == 3
    assert Category.product_count == 3


def test_empty_category_products_property(reset_counts):
    category = Category("Category1", "Description1")
    products = category.products
    assert products == []


def test_product_creation(reset_counts, capsys):
    p1 = Product("Product1", "Description1", 100.0, 10)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами" in captured.out
    assert p1.name == "Product1"
    assert p1.description == "Description1"
    assert p1.price == 100.0
    assert p1.quantity == 10
    assert BaseProduct.product_count == 1


def test_product_addition(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    p2 = Product("Product2", "Description2", 200.0, 5)
    total_value = p1 + p2
    assert total_value == (p1.price * p1.quantity + p2.price * p2.quantity)


def test_product_addition_invalid_type(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    with pytest.raises(TypeError):
        p1 + "InvalidType"


def test_price_setter_positive(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    p1.price = 150.0
    assert p1.price == 150.0


def test_price_setter_negative(reset_counts, capsys):
    p1 = Product("Product1", "Description1", 100.0, 10)
    p1.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не может быть отрицательной." in captured.out
    assert p1.price == 100.0


def test_repr():
    p1 = Product("Product1", "Description1", 100.0, 10)
    assert "Product" in repr(p1)
    assert "name" in repr(p1)
    assert "price" in repr(p1)


def test_new_product():
    data = {"name": "Product1", "description": "Description1", "price": 100.0, "quantity": 10}
    p1 = Product.new_product(data)
    assert isinstance(p1, Product)
    assert p1.name == "Product1"


def test_product_creation_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    assert category.middle_price() == (180000.0 + 210000.0 + 31000.0) / 3


def test_middle_price_empty_category():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
