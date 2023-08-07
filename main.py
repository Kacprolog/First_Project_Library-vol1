# Przywitanie użytkownika
def greet_user(username):
    print(f'Witaj {username.title()} w elektronicznym zbiorze książek. ')

username = input("Podaj imię: ")
greet_user(username)

#Rekordy podstawowe
book1 = dict(title="Upadek gondolinu", author="J.R.R. Tolkien", availability=5)
book2 = dict(title="Beren i Lúthien", author="J.R.R. Tolkien", availability=2)
book3 = dict(title="Silmarillion", author="J.R.R. Tolkien", availability=3)
book4 = dict(title="Ego to twój wróg", author="Ryan Holiday", availability=10)
library = [book1, book2, book3, book4]

# Wyszukiwanie książek w bibliotece
def find_book(library, title=None, author=None, availability=None):
    for book in library:
        if (title is None or book['title'].lower() == title.lower()) and \
                (author is None or book['author'] == author) and \
                (availability is None or book['availability'] == availability):
            return book
    return None
search_title = input('Jakiej książki szukasz?: ')
result = find_book(library, title=search_title)
if result:
    print(f"Znaleziono książkę: {result['title']} autorstwa {result['author']}")
else:
    print("Nie znaleziono książki.")

# Dodawanie książek do biblioteki
def add_book(library, title, author, availability):
    new_book = dict(title=title, author=author, availability=availability)
    library.append(new_book)

title = input("Podaj tytuł książki, którą chcesz dodać do zbioru: ")
author = input("Podaj autora książki: ")
availability = int(input("Podaj dostępność książki: "))

add_book(library, title, author, availability)
print(library)


# Wyświetlanie pełnego zbioru (trzeba dodać numerację rekordow)
def full_collection(library):
    for title in library:
        print(title)
full_collection(library)

# Usuwanie książek z biblioteki
def del_book(library, title=None, author=None, availability=None):
    for book in library[:]:
        if (title is None or book['title'] == title) and \
                (author is None or book['author'] == author) and \
                (availability is None or book['availability'] == availability):
            library.remove(book)
del_book(library, title="Upadek gondolinu")
print(library)
