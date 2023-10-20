import calendar

number = int(input("write one number from 1 to 12: "))
def get_month(number):
    if number == 1:
        return "January"
    elif number == 2:
        return "February"
    elif number == 3:
        return "March"
    elif number == 4:
        return "April"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June"
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "September"
    elif number == 10:
        return "October"
    elif number == 11:
        return "November"
    elif number == 12:
        return "December"
    else:
        return "Invalid input. Please enter a number between 1 and 12."
month = get_month(number)
print("The month corresponding to the number", number, "is", month)



