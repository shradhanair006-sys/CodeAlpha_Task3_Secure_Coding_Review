


# Task 3 - Secure Coding Review

## Project Overview
A Python-based login application reviewed for
common security vulnerabilities.

## Programming Language
Python

## Tools Used
- Visual Studio Code
- Python
- Bcrypt

## Vulnerabilities Identified

1. Hardcoded Credentials
   - Credentials were directly written in the source code.
   - Recommendation: Store credentials securely.

2. Weak Password
   - The original password was easy to guess.
   - Recommendation: Enforce strong password policies.

3. Plain Text Password Handling
   - Original code used direct password comparison.
   - Recommendation: Use secure password hashing.

## Security Improvements
- Used getpass to hide password input.
- Used bcrypt for password hashing.
- Used bcrypt.checkpw() for password verification.

## Files Included
- login_app.py
- secure_login.py
- requirements.txt
- README.md

## Conclusion
This project demonstrates how code review
can identify security weaknesses and how
secure coding practices can improve an application.
