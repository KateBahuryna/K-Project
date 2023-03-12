# ЗАДАНИЕ 2
# Создать класс книга Book, который будет хранить следующую информацию о книге:
# name - название
# description - краткое описание
# pages - количество страниц
# author - автор
# price - цена
#
# Также у класса должны быть методы:
# to_dict(self) - возвращает информацию о книге в виде словаря
# contains_word(self, word) - возвращает True, если в названии
# или описании есть переданное слово
# Также А также между объектами этого класса должны поддерживаться операции
# >, <, >=, <=, которые сравнивают книги по количеству страниц
# ==, != - сранивают совпадает ли вся информация у двух книга
#
# Также создать класс Library, который будет иметь свойство books -
# при инициализации пустой список.
# Также добавить методы
# add_book(self, book) # добавляет книгу в свойство books
# get_books(self) # возвращает списко с информацией о всех книгах,
# каждая информация о книге должна быть в виде словаря
# remove_book(self, book) - удаляет книгу по значнию из свойства books
# find_the_biggest_book(self) - возвращает книгу, в которой больше всего
# страниц, если книг нет, то вызывает ошибку EmptyLibraryError
# Также класс библиотека должен поддерживать метод len(), который будет
# возвращать количество книг в библиотеке

from copy import deepcopy


class Book:
    def __init__(self, name, description, pages, author, price):
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def to_dict(self):
        res = ({'Name': self.name,
                'Description': self.description,
                'Pages': self.pages,
                'Author': self.author,
                'Price': self.price})
        return res

    def contains_word(self, word):
        if not isinstance(word, str):
            raise ValueError("The word must be type string.")
        return (word.lower() in self.name.lower() or
                word.lower() in self.description.lower())

    def __gt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages > other.pages

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages >= other.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return (self.name == other.name and
                self.description == other.description and
                self.pages == other.pages and
                self.author == other.author and
                self.price == other.price)


class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def get_book(self):
        res = [{'Name': book.name,
                'Description': book.description,
                'Pages': book.pages, 'Author': book.author,
                'Price': book.price} for book in self.book]
        return res

    def remove_book(self, book):
        self.book.remove(book)

    def find_the_biggest_book(self):
        if len(self.book) == 0:
            raise ValueError('EmptyLibraryError.')
        book_deepcopy = deepcopy(self.book)
        book_deepcopy.sort(key=lambda el: el.pages, reverse=True)
        return [book.name for book in book_deepcopy][0]

    def __len__(self):
        return len(self.book)


book1 = Book("1984", "Some description", 1200, "Orwell", 10)
book2 = Book("Learn Python", "About python", 1000, "Luhts", 49)
book3 = Book("Harry Potter", "About magic", 8000, "Rowling", 100)
print(book1.to_dict())
print(book2.to_dict())
print(book1.contains_word("rip"))

# print(book1 < book2)
# print(book1 >= book2)
# print(book1 == book2)

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
print(lib.get_book())
print(lib.find_the_biggest_book())
print(len(lib))
