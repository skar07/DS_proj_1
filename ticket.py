import config
import booked


def ticket():
    row = int(input("Please enter the row number to be checked: "))
    column = int(input("Please enter the column number to be checked: "))
    print("\n")
    for i in config.customer:
        if i["row"] == row and i["column"] == column:
            for j in i:
                print(j+": "+str(i[j]))
        else:
            print("The requested seat is not booked.")
    return
