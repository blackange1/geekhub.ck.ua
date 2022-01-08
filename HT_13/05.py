# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).

class Book(object):
    def __init__(self, title, year, count=1, authors = []) -> None:
        self.title = title
        self.year = year
        self._count = count
        self.authors = authors.copy()

    def add_count(self, count: int) -> None:
        if isinstance(count, int):
            self._count += count
        else:
            raise TypeError

    def delete_count(self, count: int) -> None:
        if isinstance(count, int):
            if count > self._count:
                print("Неможливо списати таку кількість книг")
            else:
                self._count -= count
        else:
            raise TypeError

    def print_count(self) -> None:
        print(self._count)


class Peaple(object):
    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year


class Student(Peaple):
    def __init__(self, name, year) -> None:
        super().__init__(name, year)
        self.books = []
        print(f"Створено студента {name}")

    def add_book(self, obj):
        if isinstance(obj, Book):
            self.books.append(obj)
        else:
            print("Додавати можна лише об'єкти типу Book")

    def print_books(self):
        if len(self.books) == 0:
            print("В учня не має жодної книги")
        else:
            for book in self.books:
                print(book.title, book.year, book.authors)


inform = Book("Інформатика", 2016, 20)
inform.add_count(5)
inform.print_count()
inform.delete_count(55)
inform.delete_count(5)
inform.print_count()

fizika = Book("Фізика", 2019, 1, ["Автор 1", "Автор 2"])
mathematika = Book("Геометрія", 2019, 1, ["Автор 3"])

student_1 = Student("Jack", 2000)
student_1.add_book(fizika)
student_1.add_book(mathematika)
student_1.print_books()

student_2 = Student("Oleg", 2000)
student_2.print_books()
