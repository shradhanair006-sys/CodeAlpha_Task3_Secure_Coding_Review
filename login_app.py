
# Secure Coding Review - Task 3

# Simple Login Application

username = input("Enter your username: ")
import getpass

password = getpass.getpass("Enter your password: ")

if username == "admin" and password == "admin123":
    print("Login Successful!")
else:
    print("Invalid username or password!")
