# 📚 BooksCollector: Unit Tests

Этот репозиторий содержит тесты для класса `BooksCollector`. Тесты написаны с использованием `pytest` и охватывают основные функции работы с книгами, жанрами и избранным списком.

## 🛠 Установка и запуск тестов

1. Установите зависимости (если ещё не установлены):
   ```sh
   pip install -r requirements.txt
   ```
   
2. Запустите тесты:
   ```sh
   pytest
   ```

## ✅ Реализованные тесты

### 📌 Добавление книг
- `test_add_new_book_two_books_added_successfully` — проверяет, что можно добавить две книги в коллекцию.
- `test_add_new_book_parametrized_book_added_successfully` — параметризованный тест, проверяющий, что добавленная книга появляется в списке.
- `test_add_new_book_exceeds_max_length_rejected` — проверяет, что книга с названием длиннее 40 символов не добавляется.

### 🎭 Работа с жанрами
- `test_set_book_genre_valid_genre_applied_successfully` — проверяет, что можно корректно установить жанр книги.
- `test_set_book_genre_invalid_genre_not_applied` — параметризованный тест, проверяющий, что нельзя установить недопустимый жанр.
- `test_get_books_with_specific_genre_returns_correct_list` — проверяет, что метод возвращает корректный список книг с заданным жанром.

### 👶 Фильтрация детских книг
- `test_get_books_for_children_filters_out_horror_books` — проверяет, что книги с жанром "Ужасы" не попадают в список детских.

### ⭐ Работа с избранным
- `test_add_book_in_favorites_book_added_to_favorites` — проверяет, что книга добавляется в список избранного.
- `test_delete_book_from_favorites_book_removed_successfully` — проверяет, что книгу можно удалить из списка избранного.
- `test_get_list_of_favorites_books_returns_correct_list` — проверяет, что список избранных книг возвращается корректно.

