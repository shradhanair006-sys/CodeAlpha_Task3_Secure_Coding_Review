
# Security Audit Report

## 1. Project Details
Project Name: Secure Coding Review
Language: Python
Application: Login Application

## 2. Vulnerabilities Found

### Vulnerability 1: Hardcoded Credentials
Severity: High

Description:
Username and password were directly written in the source code.

Risk:
Attackers who access the source code may discover credentials.

Remediation:
Store credentials securely outside the source code.

### Vulnerability 2: Weak Password
Severity: Medium

Description:
The original password was easy to guess.

Risk:
Attackers may guess the password through brute-force attempts.

Remediation:
Use strong passwords and enforce password policies.

### Vulnerability 3: Insecure Password Handling
Severity: Medium

Description:
The original application used direct password comparison.

Risk:
Plain-text passwords should not be stored or exposed.

Remediation:
Use bcrypt or Argon2 for password hashing.

### Vulnerability 4: Hardcoded Password (Bandit B105)

Severity: Low

Tool: Bandit Static Code Analyzer

Location: login_app.py, Line 3

Description:
Bandit detected a hardcoded password
"admin123" inside the source code.

Risk:
Anyone accessing the source code may
discover the password.

Remediation:
Avoid hardcoding passwords.
Use secure credential storage and
bcrypt password hashing.


## 3. Security Tools
- Manual Code Review
- Python
- Bcrypt

## 4. Conclusion
The code review identified security weaknesses
in the original login application.

Security improvements were implemented using
password masking and bcrypt hashing.

Further improvements are required before
using the application in production.

## 5. Final Security Scan Results

Tool Used: Bandit

Original Application (login_app.py):
- Hardcoded password detected.
- Issue: B105
- Severity: Low
- Confidence: Medium

Improved Application (secure_login.py):
- No issues identified by Bandit.

## 6. Conclusion

The code review identified security weaknesses
in the original login application.

Security improvements were implemented using
password masking and bcrypt password hashing.

Bandit static analysis was used to identify
potential security vulnerabilities.

The improved application showed no issues
during the final Bandit scan.

Further security testing is required before
using the application in production.
