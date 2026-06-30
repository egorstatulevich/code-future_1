import json
import os
from datetime import datetime


books_file = "books.json"


def load_books():
    if not os.path.exists(books_file):
        return []

    with open(books_file, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_books(books):
    with open(books_file, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(books):
    author = input("Название автора: ").strip()
    title = input("Название книги: ").strip()

    if not author or not title:
        print("Автор и название книги не должны быть пустыми.")
        return

    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Книга уже есть в списке.")
            return

    while True:
        try:
            rating = int(input("Добавить оценку от 1 до 5: "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Вы ввели не целое число. Повторите попытку.")

    read_date = input("Добавьте дату прочтения книги: ").strip()

    if not read_date:
        read_date = datetime.now().strftime("%d.%m.%Y")

    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "read_date": read_date
    }

    books.append(book)
    save_books(books)

    print("Книга успешно добавлена!")


def show_books(books):
    if not books:
        print("Список книг пуст.")
        return

    print("\nСписок книг:")

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. {book['author']} - {book['title']}, "
            f"оценка: {book['rating']}, дата: {book['read_date']}"
        )


def book_rating_avg(books):
    if not books:
        print("Список книг пуст. Невозможно рассчитать средний балл.")
        return 0

    total_rating = sum(book["rating"] for book in books)
    avg_rating = total_rating / len(books)

    print(f"Средний рейтинг всех книг: {avg_rating:.2f}")

    return avg_rating


def author_stats(books):
    if not books:
        print("Список книг пуст.")
        return

    stats = {}

    for book in books:
        author = book["author"]

        if author in stats:
            stats[author] += 1
        else:
            stats[author] = 1

    print("\nСтатистика по авторам:")

    for author, count in stats.items():
        print(f"{author}: {count} книг")


def delete_book(books):
    if not books:
        print("Список книг пуст.")
        return

    show_books(books)

    try:
        index = int(input("Введите номер книги для удаления: "))
    except ValueError:
        print("Введено не число.")
        return

    if 1 <= index <= len(books):
        removed_book = books.pop(index - 1)
        save_books(books)

        print(f"Книга '{removed_book['title']}' удалена.")
    else:
        print("Неверный номер книги.")


def menu():
    print("\nMenu")
    print("Добавить книгу - 1")
    print("Показать книги - 2")
    print("Показать avg оценку - 3")
    print("Статистика по авторам - 4")
    print("Удалить книгу - 5")
    print("Выход - 6")


def main():
    books = load_books()

    while True:
        menu()

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            book_rating_avg(books)
        elif choice == "4":
            author_stats(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Такого пункта меню нет.")


if __name__ == "__main__":
    main()