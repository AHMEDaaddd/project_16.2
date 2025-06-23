"""Модуль с моделями: BaseProduct, Product, Smartphone, LawnGrass, Category, Order."""

from abc import ABC, abstractmethod

from src.mixins import CreationPrintMixin


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Вернуть название продукта."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Вернуть описание продукта."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Вернуть цену продукта."""
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        """Вернуть количество продукта."""
        pass


class Product(CreationPrintMixin, BaseProduct):
    """Конкретный продукт магазина."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Создаёт объект Product."""
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def name(self) -> str:
        """Вернуть название продукта."""
        return self._name

    @property
    def description(self) -> str:
        """Вернуть описание продукта."""
        return self._description

    @property
    def price(self) -> float:
        """Вернуть цену продукта."""
        return self._price

    @property
    def quantity(self) -> int:
        """Вернуть количество продукта."""
        return self._quantity


class Smartphone(Product):
    """Класс смартфона как подтипа продукта."""

    pass


class LawnGrass(Product):
    """Класс газонной травы как подтипа продукта."""

    pass


class Category:
    """Класс категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории с продуктами."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


class Order:
    """Класс заказа: один товар, количество и расчет итоговой стоимости."""

    def __init__(self, product: Product, quantity: int):
        """Инициализация заказа."""
        self.product = product
        self.quantity = quantity

    def total_price(self) -> float:
        """Вычислить итоговую стоимость заказа."""
        return self.product.price * self.quantity
