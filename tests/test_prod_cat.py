import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def reset_counts():
    """Сбрасывает глобальные счетчики перед каждым тестом"""
    Product.product_count = 0
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Создает примеры продуктов для тестов"""
    p1 = Product("Product1", "Description1", 100.0, 10)
    p2 = Product("Product2", "Description2", 200.0, 20)
    return [p1, p2]


def test_product_creation(reset_counts):
    p1 = Product("Product1", "Description1", 100.0, 10)
    assert p1.name == "Product1"
    assert p1.description == "Description1"
    assert p1.price == 100.0
    assert p1.quantity == 10
    assert Product.product_count == 1


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


def test_product_addition(reset_counts, sample_products):
    p1 = sample_products[0]
    p2 = sample_products[1]
    total_value = p1 + p2
    assert total_value == (p1.price * p1.quantity + p2.price * p2.quantity)


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
