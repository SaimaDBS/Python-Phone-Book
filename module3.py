import datetime


def add_new_entry():
    date = input('Week Ending: (DD/MM/YEAR): ')
    try:
        weekEnding = datetime.datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        print("Sorry, that is in the incorrect format. Try again!")
        return add_new_entry()
    
    return date


print(add_new_entry())