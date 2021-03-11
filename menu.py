import config
import sys
import seats as seat
import ticket as tickets
import booked as books
import stats as stat

count = 0


def menu():
    global count
    print("Enter the number of rows:\n")
    config.x = int(input())
    print("Enter the number of seats in each row:\n")
    config.y = int(input())
    while (True):
        print('''\t    1. Show the seats\n
            2. Buy a ticket\n
            3. Statistics\n
            4. Show booked Tickets User info\n
            0. Exit ''')
        choice = int(input())
        if choice == 1:
            seats()
        elif choice == 2:
            booked()
        elif choice == 3:
            stats()
        elif choice == 4:
            ticket()
        else:
            sys.exit()
        count += 1


def seats():
    x1 = seat.Seating(config.x, config.y)
    if count == 0:
        x1.seats()
    else:
        x1.ret()
    return


def ticket():
    tickets.ticket()
    return


def stats():
    stat.stats()
    return


def booked():
    b1 = books.Book(config.x, config.y)
    b1.booking()
    return
