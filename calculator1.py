import os
import pickle

while True:
    print(" welcome to claculator ")
    print("  choose your function ")
    print("-----------------------")
    print("                       ")
    print("   enter your numbers  ")
    print("                       ")
    print("      {1} sum +        ")
    print("                       ")
    print("      {2} sub -        ")
    print("                       ")
    print("      {3} mult *       ")
    print("                       ")
    print("      {4} div /        ")
    print("                       ")
    print("      {5} exit         ")
    print("-----------------------")

    opt = int(input(" enter an option : "))
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if opt == 1 :
        jam = num1 + num2
        print("{0} + {1} = {2}".format(num1, num2, jam))
    elif opt == 2:
        sub = num1 - num2
        print("{0} - {1} = {2} ".format(num1, num2, sub))
    elif opt == 3:
        mult = num1 * num2
        print("{0} * {1} = {2} ".format(num1, num2, mult))
    elif opt == 4:
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            div = float(num1) / float(num2)
            print("{0} / {1} = {2:.2f} ".format(num1, num2, div))
    elif opt == 5:
        print("Exiting calculator...")
        break
    else:
        print("Invalid option. Please enter a valid option (1-5).")