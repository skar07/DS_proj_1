from seats import Seating
import config

x = 0
y = 0


class Book(Seating):
    def __init__(self, row, column):
        super().__init__(row, column)

    def booking(self):
        global x, y
        info = 0
        x = int(input("Please enter row of desired seat:\n"))
        y = int(input("Please enter column of desired seat:\n"))
        if config.val[x][y] != 'B':
            if(self.row*self.column <= 60):
                config.price = 10
                chi = input("Price: {}\nWould you like to purchase this seat? If yes, type yes:\n".format(
                    config.price)).lower()
                config.price = str(config.price)+"$"
                if chi == 'yes' or chi == 'Y' or chi == 'y':
                    info = details()
                    config.customer.append(info)
                    print("Booked successfully.")

                else:
                    print("Invalid entry. Try again.")

            else:
                config.half = self.row//2
                if x <= config.half:
                    config.price = 10
                    chi = input("Price: {}\nWould you like to purchase this seat? If yes, type yes:\n".format(
                        config.price)).lower()
                    config.price = str(config.price)+"$"
                    if chi == 'yes' or chi == 'Y' or chi == 'y':
                        info = details()
                        config.customer.append(info)
                        print("Booked successfully.")

                    else:
                        print("Invalid entry. Try again.")

                elif x > config.half:
                    config.price = 8
                    chi = input("Price: {}\nWould you like to purchase this seat? If yes, type yes:\n".format(
                        config.price)).lower()
                    config.price = str(config.price)+"$"
                    if chi == 'yes' or chi == 'Y' or chi == 'y':
                        info = details()
                        config.customer.append(info)
                        print("Booked successfully")

                    else:
                        print("Invalid entry. Try again.")

        else:
            print("Seat already taken. Please try again.")
            return
        config.val[x][y] = 'B'
        self.ret()


def details():
    print("Please enter the required details below")
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    gender = input("Please enter your gender: ")
    phone = input("Please enter your phone number: ")
    thisdict = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Phone": phone,
        "row": x,
        "column": y,
        "Ticket price": config.price,
    }

    return thisdict
