
import bcrypt
import getpass

# Create a new password
password = getpass.getpass("Create your password: ")

# Generate a secure password hash
hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

# Save the hash in a separate file
with open("password_hash.txt", "wb") as file:
    file.write(hashed_password)

print("Password hash saved successfully!")
