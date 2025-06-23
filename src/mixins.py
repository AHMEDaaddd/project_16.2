"""Модуль с миксинами."""


class CreationPrintMixin:
    """Миксин, который выводит информацию при создании объекта."""

    def __init__(self, name, description, price, quantity):
        """Выводит параметры созданного объекта."""
        print(
            f"Создан объект {self.__class__.__name__} с параметрами:"
            f" name='{name}', description='{description}',"
            f" price={price}, quantity={quantity}"
        )
        super().__init__()
