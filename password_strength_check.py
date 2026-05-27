from pathlib import Path

COMMON_PASSWORDS_FILE = "rockyou_1.txt"

def load_common_passwords(path = Path("common_passwords") / COMMON_PASSWORDS_FILE):
    with open(path, "r", encoding = "utf-8"):
        common_passwords = path.read_text(encoding="utf-8").splitlines()
    return common_passwords

def check_common_pattern(password: str):
    """Checks if a password follows a common pattern "letters-numbers" 
    (all the letters come first and all the following sings are numbers).\n
    Returns True when password follows the pattern and False when it does not.
    If the password only consists of letters or only consists of numbers, the function returns False."""
    return  password.isalnum() and any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and password.rstrip("0123456789").isalpha()
    
def main():
    password = input("Enter a password to check: ")
    common_passwords = load_common_passwords()
    print(len(common_passwords))

    if password in common_passwords:
        print("This is a common password!")

    pattern = check_common_pattern(password)
    if pattern:
        print("Your password follows a common 'letters-numbers' pattern :(")

    # TODO:
    # - password length
    # - uppercase letters, numbers, special signs check
    # - only letters check
    # - give suggestions
    # - password score (?)

if __name__ == "__main__":
    main()

