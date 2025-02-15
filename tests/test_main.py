import pytest
from main import Product, Category

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
