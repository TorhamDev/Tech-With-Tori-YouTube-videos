#! /usr/bin/python3

password = "1234"

input_password = input("Enter Password:")

show_password = None


if input_password == password:
    show_password = True

elif input_password != password:
    print("Get lost, rude hacker!")


else:
    show_password = None


if show_password != False:
    print("Hello, dear admin. The top secret password is the OWASP-Top10-4 database.")
