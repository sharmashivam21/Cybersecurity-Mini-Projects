import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Weak: Include at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Include at least one special character."
    return "Strong Password ✅"

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))
