import pytest
from main import BooksCollector

class TestBooksCollector:

#1
    def test_add_new_book_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        assert ('Гарри Поттер и философский камень') in collector.books_genre
#2
    def test_add_new_book_false(self):
        collector = BooksCollector()

        collector.add_new_book('Триста спартанцев: Леонид-царь, его первый друг, его второй друг, его третий друг, брат жены, кузен со свадьбы лучшего друга номер два, тот парень с кольцами в носу')
        assert ('Триста спартанцев: Леонид-царь, его первый друг, его второй друг, его третий друг, брат жены, кузен со свадьбы лучшего друга номер два, тот парень с кольцами в носу') not in collector.books_genre

#3
    @pytest.mark.parametrize('name', ['Убить пересмешника', 'Имя розы', 'Садоводство для чайников'])
    def test_add_new_book_list_true(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert (name) in collector.books_genre

#4
    def test_set_book_genre_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

 #5
    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()

        collector.add_new_book('Имя розы')
        collector.set_book_genre('Имя розы', 'Детективы')
        assert 'Имя розы' in collector.get_books_with_specific_genre('Детективы')

    #6
    def test_get_books_for_children_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert 'Гарри Поттер и философский камень' in collector.get_books_for_children()

    #7

    def test_get_books_for_children_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Имя розы')
        collector.set_book_genre('Имя розы', 'Детектив')
        assert 'Имя розы' not in collector.get_books_for_children()

#8
    @pytest.mark.parametrize("name", ['Убить пересмешника', 'Имя розы', 'Садоводство для чайников'])
    def test_add_book_in_favorites_true(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

#9
    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Sweetyгуруми')
        collector.add_book_in_favorites('Sweetyгуруми')
        collector.delete_book_from_favorites('Sweetyгуруми')
        assert 'Sweetyгуруми' not in collector.get_list_of_favorites_books()

#10
    def test_add_new_book_duplicate_name_false(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Sweetyгуруми')
        collector.add_new_book('Гарри Поттер и философский камень')
        assert len(collector.books_genre) == 2