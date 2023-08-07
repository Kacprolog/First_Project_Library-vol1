book1 = dict(title="Upadek gondolinu", author="J.R.R. Tolkien", availability=5)
book2 = dict(title="Beren i Lúthien", author="J.R.R. Tolkien", availability=2)
book3 = dict(title="Silmarillion", author="J.R.R. Tolkien", availability=3)
book4 = dict(title="Ego to twój wróg", author="Ryan Holiday", availability=10)
library = [book1, book2, book3, book4]

#dodawanie książek do biblioteki
def add_book(library, title, author, availability):
    new_book = dict(title=title, author=author, availability=availability)
    library.append(new_book)

add_book(library, "Hobbit", "J.R.R. Tolkien", 4)

#Wyszukiwanie książek w bibliotece
def find_book(library, title=None, author=None, availability=None):
    found_books = []
    for book in library:
        if (title is None or book['title'] == title) and \
           (author is None or book['author'] == author) and \
           (availability is None or book['availability'] == availability):
            found_books.append(book)
    return found_books

find_book(library, "J.R.R. Tolkien" )

#Usuwanie książek z biblioteki
def del_book(library, title=None, author=None, availabilityc=None):
    for book in library[:]:
        if (title is None or book['title'] == title) and \
           (author is None or book['author'] == author) and \
           (availability is None or book['availability'] == availability):
            library.remove(book)
