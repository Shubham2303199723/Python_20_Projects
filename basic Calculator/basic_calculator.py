# define the functions needed sub, add, multiply, divide
# print options to user
# ask for values
# call the function
# while loop until user want to exit

def sub(a,b):
    return a-b

def sum(a,b):
    return a+b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b

while True:
    print(" 1. +\n 2. -\n 3. *\n 4. /\n 5. exit \n what you want to do:- ")
    user_input = str(input())
    if user_input == '+':
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        print("Your Answer", sum(a,b))
    elif user_input == '-':
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        print("Your Answer", sub(a,b))
    elif user_input == '*':
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        print("Your Answer", multi(a,b))
    elif user_input == '/':
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        print("Your Answer", divide(a,b))
    else:
        break
