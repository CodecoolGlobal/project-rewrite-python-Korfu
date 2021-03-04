from distlib.compat import raw_input
import os

def min(x, y):
    if x > y:
        return y
    else:
        return x


def max(values_list):
    result = values_list[0]
    for item in values_list:
        if item > result:
            result = item
    return result

def len(values_list):
    result = 0
    for _ in values_list:
        result += 1
    return result


def multiply(x, y):
    count = 0
    result = 0
    while True:
        count += 1
        result += x
        if count == y:
            return result


def pow(x, y):
    pass
    count = 1
    result = x
    while True:
        count += 1
        result *= x
        if count == y:
            return result

def divmod(x, y):
    count = 0
    while True:
        x = x - y
        count += 1
        if x == y:
            return count
        if x < y:
            return count, x

def print_menu():
    print("1) minimum")
    print("2) maximum")
    print("3) length")
    print("4) multiplication")
    print("5) power")
    print("6) division")

if __name__ == '__main__':
    user_input = None
    while(user_input != "Q"):
        print_menu()
        user_input = input("Choose your operation: ")
        result = None
        if user_input == '1':
            x, y = list(map(int,("Provide two numbers you want to find minimum of").split()))
            result = min(x, y)
        elif user_input == '2':
            list = list(map(int, input("Provide list of numbers you want to find maximum of: ").split()))
            result = max(list)
        elif user_input == '3':
            list = list(map(int, input("Provide list of numbers you want to find maximum of: ").split()))
            result = len(list)
        elif user_input == '4':
            x, y = list(map(int,raw_input("Provide two numbers you want to multiply").split()))
            result = multiply(x, y)
        elif user_input == '5':
            x, y = list(map(int,raw_input("Provide two numbers you want to power").split()))
            result = pow(x, y)
        elif user_input == '6':
            x, y = list(map(int,raw_input("Provide two numbers you want to divmod").split()))
            result = divmod(x, y)
        print(" ")
        print(result)
        input("Click any key to continue")
