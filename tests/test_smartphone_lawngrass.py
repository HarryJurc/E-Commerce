import pytest
from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_product_addition_same_type():
    phone1 = Smartphone("Phone1", "Smartphone Description", 50000, 5, "ModelX", 9.5, 128, "Black")
    phone2 = Smartphone("Phone2", "Smartphone Description", 60000, 3, "ModelY", 8.0, 256, "White")
    assert phone1 + phone2 == (phone1.price * phone1.quantity + phone2.price * phone2.quantity)


def test_product_addition_different_type():
    phone = Smartphone("Phone1", "Smartphone Description", 50000, 5, "ModelX", 9.5, 128, "Black")
    grass = LawnGrass("Grass1", "Lawn Grass Description", 200, 10, "Russia", 14, "Green")
    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_add_valid_product():
    category = Category("Electronics", "Various electronic devices")
    phone = Smartphone("Phone1", "Smartphone Description", 50000, 5, "ModelX", 9.5, 128, "Black")
    category.add_product(phone)
    assert len(category.products) == 1


def test_category_add_invalid_product():
    category = Category("Electronics", "Various electronic devices")
    with pytest.raises(TypeError):
        category.add_product("NotAProduct")
