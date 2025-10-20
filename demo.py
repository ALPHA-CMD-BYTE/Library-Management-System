# demo.py
from operations import *

print("=== DEMO: Library Management System ===\n")

print(add_book(books, "001", "Python Basics", "Osman sheriff", "Fiction", 3, genres))
print(add_book(books, "002", "Networking 101", "Alpha Sheriff", "Education", 2, genres))

print(add_member(members, 1, "Selwyn", "selwyn@gmail.com"))
print(add_member(members, 2, "Solomon", "solomon@gmail.com"))

print(borrow_book(books, members, 1, "001"))
print(borrow_book(books, members, 1, "002"))
print(return_book(books, members, 1, "001"))

print(delete_book(books, "002"))
print(delete_member(members, 2))
