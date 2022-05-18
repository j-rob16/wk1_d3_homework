def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(num):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[num -1]

def number_to_short_month_name(num):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[num -1]

def volume_of_cube(side):
    return side ** 3

def reverse_this_string(string):
    return string[::-1]

def convert_fahrenheit(ftemp):
    ctemp = (ftemp -32) * (5/9)
    return round(ctemp, 1)