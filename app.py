from models import (Base, session, 
                    Book, engine)
import datetime
import csv
import time

def menu():
    while True:
        print("""
              \nPROGRAMMING BOOKS
              \r1) Add book
              \r2) View all books
              \r3) Search for book
              \r4) Book Analysis
              \r5) Exit""")
        choice = input("What would you like to do? ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            input("""
                  \rEnter only one of the options above.
                  \rEnter 1, 2, 3, 4, or 5.
                  \rPress enter to try again.""")
  

def clean_date(date_str): # date_str is any parameter variable. self-defined
    # lists are zero indexed.
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November",
              "December"]
    split_date = date_str.split(" ")
    
    try:
        month = int(months.index(split_date[0]) + 1) # plus 1 because months are 1-indexed
        day = int(split_date[1].split(",")[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
        return return_date

#    except ValueError as identifier:
 #       print("Day is out of range for the month")
#    except expression as identifier:
#        print("Date is not in the correct format")
#        pass
    except ValueError:
        input('''
              \n****** DATE ERROR ******
              \rThe date format should include a valid Month Day, Year from the past.
              \rEx: January 13, 2003
              \rPress enter to try again.
              \r*************************''')
        return
#        pass
    else:
        return return_date
#        pass
    
   # return
    
    #print(split_date)
    # find the index 0 from the months list. which gives a number one less than needed. because lists are zero index
    month = int(months.index(split_date[0]) + 1) # plus 1 because months are 1-indexed
#    day = int(split_date[1].split(",")[0])
    day = int(split_date[1].split(",")[0])
    year = int(split_date[2])
    #year = int(split_date[2].split(",")[0])
    # return a daytime.date object
    #return datetime.date(year, month, day)
    #datetime.date()
   # datetime.date() # year, month, day have to be integers. month variable from above and its value must be all integers. which can be done with a wrapper
    #print(day)
    return datetime.date(year, month, day)


def clean_price(price_str):
    try:
        price_float = float(price_str)
    except ValueError:
        input('''
              \n****** PRICE ERROR ******
              \rThe price should be a number without a currency symbol.
              \rEx: 10.99
              \rPress enter to try again
              \r*************************''')
    else:
    # convert the number to a float because it has a decimal point in the .csv file

    #print(price_float)
        return int(price_float * 100)  # convert to cents by multiplying by 100


def add_csv():
    with open("suggested_books.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none() # return none if there isnt a book
            
            # conditional statement to check if book is still in the db 
            if book_in_db == None: # must be aware the db has dubplicates
                
            #print(row)
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "1":
            # add book
            title = input("Title: ")
            author = input("Author: ")
            date_error = True # while date error
            while date_error:
                date = input('Published Date (Ex: October 25, 2017): ') # date in specific format for the date library/module. all integers
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input("Price: (Ex: 25.64): ") # price in cents
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, published_date=date, price=price)
            session.add(new_book)
            session.commit()
            print("Book was added to the database.")
            time.sleep(1.5)
        elif choice == "2":
            # view books
            pass    
        elif choice == "3":
            # search books
            pass
        elif choice == "4":
            # analysys
            pass
        else:
            print("Goodbye!")
            app_running = False


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    app()
    #add_csv()
    #clean_date("25.64")
    #clean_price("28.84")
    for book in session.query(Book):
        print(book)