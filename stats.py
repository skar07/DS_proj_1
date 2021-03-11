
import config
import booked


def stats():
    inc = 0
    first_tick = 0
    second_tick = 0
    tickets = 0
    curr_inc = 0
    total_inc = 0
    total_seat = config.x*config.y
    for i in config.val:
        for j in i:
            if j == 'B':
                tickets += 1
    percent = (tickets / total_seat) * 100
    total_inc = total_seat*10
    if total_seat <= 60:
        curr_inc = tickets * 10
        inc = curr_inc
    else:
        length = len(config.val)//2
        first_half = config.val[0:length]
        for j in first_half:
            for i in j:
                if i == 'B':
                    first_tick += 1
        curr_inc = first_tick * 10
        inc = curr_inc
        second_half = config.val[length:]
        for j in second_half:
            for i in j:
                if i == 'B':
                    second_tick += 1
        curr_inc = second_tick * 8
        inc += curr_inc

    print("Number of purchased tickets: {}".format(tickets))
    print("Percentage: {:.2f}%".format(percent))
    print("Current income: {}$".format(inc))
    print("Total income: {}$".format(total_inc))
    return
