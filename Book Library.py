from peewee import *
import getpass

from pip._vendor.distlib.compat import raw_input

db = SqliteDatabase("books.db")  # CREATE DATABASE my_dba


class Books(Model):  # CREATE TABLE users
    name = CharField(max_length=255)
    quantity = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([Books], safe=True)


def store_books(books_name, books_quantity):
    Books.create(name=books_name, quantity=int(books_quantity))


def update_books(books_name, books_quantity):
    old_books = Books.get(name=books_name)
    if old_books:
        old_books.quantity = int(books_quantity)
        old_books.save()
    else:
        print("Current Book is not available in Library! Check again later.")


def delete_books(books_name):
    old_books = Books.get(name=books_name)
    if old_books:
        old_books.delete_instance()
    else:
        print("Current Book is not available in Library! Check again later.")


def show_books():
    return Books.select()


while True:
    print("------------------------------------Welcome To The UAP Library------------------------------------")
    print("Enter Log in Option:\n")
    print("A. Admin Login\nB. Student Login\n\n")
    print("--------------------------------------------------------------------------------------------------")
    log = input("Select Option, 'X' for exit: ")
    if log.lower() == "x":
        break
    else:
        if log.lower() == "a":
            print("------------------------------------Welcome To The UAP Library------------------------------------")
            print("-------------------------------------------Admin Login--------------------------------------------")

            password = getpass.getpass(prompt="Enter Password : ", stream=None)
            #password = raw_input()

            if password == 'rizwan':
                print("Password Accepted!\n")

                print(
                    "------------------------------------Welcome To The UAP Library------------------------------------")
                print(
                    "-------------------------------------------Admin Login--------------------------------------------")
                print("A. Store Book\nB. Update Book(s)\nC. Remove Book(s)\nD. Show Books\n")
                print(
                    "--------------------------------------------------------------------------------------------------")
                n = input("\n\n\nEnter a choice, 'X' for exit: ")
                if n.lower() == "x":
                    break
                else:
                    if n.lower() == "a":
                        books = input("Enter The Book Name: ")
                        quantity = input("Enter The Book Quantity: ")
                        store_books(books, quantity)
                        print("Book has been stored.\n\n\n\n")
                    elif n.lower() == "b":
                        books = input("Enter The Book Name for Updating: ")
                        quantity = input("Enter New Quantity For Current Book: ")
                        update_books(books, quantity)
                        print("Book Updated Successfully!!!\n\n\n\n")
                    elif n.lower() == "c":
                        books = input("Enter The Book(s) name to remove from Library: ")
                        delete_books(books)
                        print("Book Removed Successfully!!!\n\n\n\n")
                    elif n.lower() == "d":
                        books = show_books()
                        if books:
                            for Books in books:
                                print("{} => {}".format(Books.name, Books.quantity))
                        else:
                            print("Library is Empty\n\n\n\n")
                    else:
                        print("Invalid Input.")
            else:
                print("Invalid Password!")
                break
        ####################################################STUDENT###################################################
        elif log.lower() == "b":
            print("------------------------------------Welcome To The UAP Library------------------------------------")
            print("------------------------------------------Student Login-------------------------------------------")
            print("A. Show Books\nB. Take Book\n")
            print("--------------------------------------------------------------------------------------------------")
            n = input("\n\n\nEnter Choice, 'X' for exit: ")
            if n.lower() == "x":
                break
            else:
                if n.lower() == "a":
                    books = show_books()
                    if books:
                        for Books in books:
                            print(
                                "Name of the Book = {} >>> Quantity Available = {}".format(Books.name, Books.quantity))
                    else:
                        print("Library is Empty\n\n\n\n")
                elif n.lower() == "b":
                    books = input("Enter The Book Name to take: ")
                    quantity = input("Enter Quantity For Current Book: ")
                    update_books(books, quantity)
                    print("\n\nBook Loaned! Return before due date!\n\n\n\n")

                else:
                    print("Invalid Input.")
