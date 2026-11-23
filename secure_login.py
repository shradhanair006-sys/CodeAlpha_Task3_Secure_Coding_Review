


import bcrypt
import getpass

# Secure Login Application

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Read the stored password hash
try:
    with open("password_hash.txt", "rb") as file:
        stored_password = file.read()

    # Verify the password
    if username == "admin" and bcrypt.checkpw(
        password.encode(), stored_password
    ):
        print("Login Successful!")
    else:
        print("Invalid username or password!")

except FileNotFoundError:
    print("Password hash file not found. Run setup_password.py first.")