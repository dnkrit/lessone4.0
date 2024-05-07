class Author():
    def __init__(self, name, natioanality):
        self.name = name
        self.nationality = natioanality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f'{self.title}, {self.author.name}')


author = Author('Лев Толстой', 'Русский')
book = Book('Война и мир', author)

print(author.name)
book.get_info_book()


class Cow(Animal):
    def make_sound(self):
        print('Муу')


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()
