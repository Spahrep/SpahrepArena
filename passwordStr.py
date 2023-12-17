import re

def checkPass(password,message):
    # Setting the criteria for a strong password
    min_length = 8
    max_length = 256
    has_uppercase = re.search(r"[A-Z]", password)
    has_lowercase = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>\_\-\=\+\]\[]", password)
    message = ""

    # Checking the password against each criterion
    if len(password) < min_length or len(password) > max_length:
        message +=  "Password must be between 8 and 256 characters long.\n"
    if not has_uppercase:
        message += "Password must contain at least one uppercase letter.\n"
    if not has_lowercase:
        message += "Password must contain at least one lowercase letter.\n"
    if not has_digit:
        message += "Password must contain at least one digit.\n"
    if not has_special_char:
        message += "Password must contain at least one special character.\n"

    if message == "":
        message = "Password Accepted"
        return True
    print(message)
    return False


