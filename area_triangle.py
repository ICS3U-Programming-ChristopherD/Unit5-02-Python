#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Nov.24, 2022
# This program calculates the area of a triangle
# using a function

# Defines the triangle area calculator
def AreaCalculator(base, height):

    # Calculates the area using the base and height
    area = base * height / 2
    print(f"The area of the triangle is {area}cm^2")


def main():

    while True:

        # Asks for the base and height of the triangle.
        try:
            user_base = float(input("Enter the base of the triangle (in cm): "))
            user_height = float(input("Enter the height of the triangle (in cm): "))

        # If any inputs are not numbers, the program will restart
        except:
            print("You must enter a number for the base and height.")
            input("Enter any key to restart: ")
            continue
        else:

            # Calls the area calculator function with the base and height as arguments
            AreaCalculator(user_base, user_height)

            # If the user enters 'q', the program quits. Otherwise, the program restarts
            user_restart = input("Enter 'q' to quit, enter any other key to restart: ")
            if user_restart == "q":
                break


if __name__ == "__main__":
    main()
