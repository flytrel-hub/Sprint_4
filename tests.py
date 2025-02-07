import pytest


class TestBooksCollector:

    def test_add_new_book_two_books_added_successfully(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "1984", "Мастер и Маргарита"])
    def test_add_new_book_parametrized_book_added_successfully(self, books_collector, book_name):
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.get_books_genre()

    def test_add_new_book_exceeds_max_length_rejected(self, books_collector):
        long_name = "А" * 41
        books_collector.add_new_book(long_name)
        assert long_name not in books_collector.get_books_genre()

    def test_set_book_genre_valid_genre_applied_successfully(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert books_collector.get_book_genre("Гарри Поттер") == "Фантастика"

    @pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Роман"), ("1984", "Поэзия")])
    def test_set_book_genre_invalid_genre_not_applied(self, books_collector, book_name, genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre_returns_correct_list(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.add_new_book("Дюна")
        books_collector.set_book_genre("Гарри Поттер", "Фантастика")
        books_collector.set_book_genre("Дюна", "Фантастика")
        assert books_collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер", "Дюна"]

    def test_get_books_for_children_filters_out_horror_books(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.add_new_book("Оно")
        books_collector.set_book_genre("Гарри Поттер", "Фантастика")
        books_collector.set_book_genre("Оно", "Ужасы")
        assert books_collector.get_books_for_children() == ["Гарри Поттер"]

    def test_add_book_in_favorites_book_added_to_favorites(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_removed_successfully(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.add_book_in_favorites("Гарри Поттер")
        books_collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_correct_list(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        books_collector.add_new_book("Дюна")
        books_collector.add_book_in_favorites("Гарри Поттер")
        books_collector.add_book_in_favorites("Дюна")
        assert set(books_collector.get_list_of_favorites_books()) == {"Гарри Поттер", "Дюна"}
