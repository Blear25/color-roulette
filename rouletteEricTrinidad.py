"""
Program Summary: This program is a roulette game where the user will input a random number and the
color wheel will respond with the color the number lands on.
IPO:
  Input: The user will input a number from 0 - 39
  Processing: The program will then record the number and spin the color wheel to the corresponding
  number pocket
  Output: The program will output the color to be either green, black, or red from the user's input.
"""

#This function determines whether a number is even or odd

def even_or_odd(num):
    return num % 2

#This is where the user will input a number from 0 - 39

def game():
    while True:
        num = input("Please enter pocket number (0-36): ")
        if num.isdigit():
            num = int(num)
            result = even_or_odd(num)

# The wheel returns green if user inputs 0
            if (int(num) == 0):
                print("\nThe Color of the Wheel Pocket is Green")
                return main()

# The wheel will return either black or red depending on user's input between 1 - 36
            elif (int(num) >= 1 and int(num) <= 10) or (int(num) >= 19 and int(num) <= 28):
                if result == 0:
                    print("\nThe Color of the Pocket Wheel is Black")

                else:
                    print("\nThe Color of the Pocket Wheel is Red")
                return main()

            elif (int(num) >= 11 and int(num) <= 18) or (int(num) >= 29 and int(num) <= 36):
                if result == 0:
                    print("\nThe Color of the Pocket Wheel is Red")

                else:
                    print("\nThe Color of the Pocket Wheel is Black")
                return main()

# This will appear if the user inputs anything other than an integer
            else:
                print("        Error ... Invalid pocket. Try again\n")
        else:
            print("        Error ... Invalid pocket. Try again\n")

# This function will call on the roulette game

def main():
    print(">>>\n"
          "Roulette Wheel Colors App ... \n")
    game()

if __name__ == "__main__":
    main()


