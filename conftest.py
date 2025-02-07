import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    """Фикстура для создания нового экземпляра BooksCollector перед каждым тестом."""
    return BooksCollector()
