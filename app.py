from models import (Base, session, 
                    Book, engine)
import datetime
import csv


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
    # convert the number to a float because it has a decimal point in the .csv file
    price_float = float(price_str)
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
            pass
        elif choice == "2":
            pass    
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Goodbye!")
            app_running = False


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #app()
    add_csv()
    #clean_date("25.64")
    #clean_price("28.84")
    for book in session.query(Book):
        print(book)