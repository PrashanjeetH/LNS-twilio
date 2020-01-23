import sys
from collections import namedtuple


# FUNCTION TO SAVE BOOK TO FILE
def SaveBook(book):
    f = open("BookData.csv","a+")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + '\n')
    f.close()


#  FUNCTION TO RETRIEVE A SINGLE BOOK RECORD FROM THE DATABASE
def GetRecord(input_id):
     with open("BookData.csv", "r") as f:
        for line in f:
            line = line.rstrip()
            id, title, author, isbn = line.split(",")
            if (id == input_id):
                return line


#  FUNCTION TO ADD A BOOK TO THE DATABASE
def AddBook():
    Book = namedtuple("Book", "ID Title Author ISBN")
    id = input("Enter the ID: ")
    title = input("Enter title of book: ")
    author = input("Enter name of author: ")
    isbn = input("Enter ISBN: ")
    newBook = Book(id, title, author, isbn)
    SaveBook(newBook)
    print("Book was added successfully")


#  FUNCTION DISPLAY DETAILS OF A PARTICULAR BOOK
def DisplayBook():
    input_id = input("Enter the ID of book to display: ")
    id,title,author,isbn = GetRecord(input_id).split(",")
    if (id == input_id):
        print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))


# FUNCTION TO DELETE A BOOK FROM THE DATABASE
def DeleteBook():
    input_id = input("Enter the ID of the book to delete: ")
    f = open("BookData.csv","r+")
    d = f.readlines()
    f.seek(0)
    for line in d:
        record = line.rstrip()
        id, title, author, isbn = record.split(",")
        if id != input_id:
            f.write(line)
    f.truncate()
    f.close()
    print("Book was successfully deleted from the database!")


# FUNCTION TO VIEW ALL BOOKS IN THE DATABASE
def ViewBooks():
         with open("BookData.csv","r") as f:
             for line in f:
                 line = line.rstrip()
                 id,title,author,isbn = line.split(",")
                 if not line: continue
                 print('{0: <5}'.format(id) + '{0: <35}'.format(title) + '{0: <25}'.format(author) + '{0: <15}'.format(isbn))


#  FUNCTION TO SEARCH FOR A BOOK IN THE DATABASE
def Search():
    criteria = input("Enter a search criteria: ")
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             if line.upper().find(criteria.upper()) != -1:
                 id,title,author,isbn = line.split(",")
                 print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))


# GET THE TOTAL NUMBER OF BOOKS
def GetTotal():
        return sum(1 for line in open('BookData.csv'))


# FUNCTION TO DISPLAY THE MENU
def DisplayMenu():
    print("CHOOSE AN OPERATION. ")
    print("1. ADD A BOOK")
    print("2. DISPLAY BOOK DETAILS")
    print("3. DELETE A BOOK")
    print("4. VIEW BOOKS")
    print("5. SEARCH FOR BOOK")
    print("6. GET TOTAL NUMBER")
    print("7. EXIT")

# *********************** BEGINING OF MAIN PROGRAM *******************
DisplayMenu()

# GET USER CHOICE
choice = input("Select an operation (1,2,3,4,5,6,7): ")

# EXIT THE PROGRAM IF THE INPUT IS 7
if choice == '7':
   sys.exit()


if choice == '1':
    AddBook()

elif choice == '2':
    DisplayBook()

elif choice == '3':
    DeleteBook()

elif choice == '4':
    ViewBooks()

elif choice == '5':
    Search()

elif choice == '6':
    print(GetTotal())

else:
   print("Invalid input")
