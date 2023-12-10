from src import password_utils as pu
from src import password_generator as pg

def main():
    print("Welcome to the Advanced Password Generator!")
    length = int(input("How long would you like the password to be? "))
    use_advanced = pu.ask_yes_no("Would you like to include an advanced character set (lowercase/uppercase/special symbols)?")
    use_custom_chars = pu.ask_yes_no("Would you like to specify a custom character set?")
    custom_chars = input("Enter the custom characters: ") if use_custom_chars else None
    strength = pu.ask_strength()
    pronounceable = pu.ask_yes_no("Do you want a pronounceable password?")
    
    password = pg.generate_password(length, use_advanced, strength, pronounceable, custom_chars)
    print("Your generated password is:", password)
    print("Estimated password entropy:", pg.calculate_entropy(password))

if __name__ == "__main__":
    main()
