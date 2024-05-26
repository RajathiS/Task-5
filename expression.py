import re
def validate_input(input_str, input_type):
    patterns = {
        "email": r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        "bd_mobile": r'^\+8801[3-9]\d{8}$',
        "us_telephone": r'^\+1\d{10}$',
        "password": r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    }
    if input_type not in patterns:
        return False

    pattern = patterns[input_type]
    return bool(re.match(pattern, input_str))

print(validate_input("guvi@gmail.com", "email"))
print(validate_input("+8801712345678", "bd_mobile"))
print(validate_input("+11234567890", "us_telephone"))
print(validate_input("Aa1@abcdefghijklm", "password"))

print(validate_input("invalid_email.com", "email"))
print(validate_input("+880123456789", "bd_mobile"))
print(validate_input("1234567890", "us_telephone"))
print(validate_input("a1A@abcdefghijklm", "password"))
