#!/usr/bin/env python3
# Created By: chanella
# Date: March 27, 2025
# This program uses a try program


def main():
    # this program uses a try statement

    # get the number from the user
    integer_as_string = input("Enter an integer: ")
    print("")

    #
    try:
        integer_as_integer = int(integer_as_string)
        print("You an integer correctly")
    except Exception:
        print("This was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
