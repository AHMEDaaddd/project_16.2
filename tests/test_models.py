from src.models import Category, LawnGrass, Order, Product, Smartphone


def test_product_creation():
    product = Product("Test", "Desc", 1000.0, 3)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 1000.0
    assert product.quantity == 3


def test_smartphone_is_product():
    phone = Smartphone("iPhone", "desc", 500.0, 2)
    assert isinstance(phone, Product)


def test_lawngrass_is_product():
    grass = LawnGrass("Трава", "описание", 120.0, 10)
    assert isinstance(grass, Product)


def test_category_counting():
    p1 = Product("P1", "D", 100.0, 1)
    p2 = Product("P2", "D", 200.0, 2)
    start_category = Category.category_count
    start_product = Category.product_count
    cat = Category("Cat", "Desc", [p1, p2])
    assert Category.category_count == start_category + 1
    assert Category.product_count >= start_product + 2


def test_order_total():
    p = Product("Phone", "desc", 15000.0, 3)
    order = Order(p, 2)
    assert order.total_price() == 30000.0
