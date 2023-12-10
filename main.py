import password_generator as pg

def main():
    print("Welcome to the Advanced Password Generator!")

    # we're gonna ask the user for the length
    length = int(input("How long would you like the password to be? "))
    # character set
    use_advanced = ask_yes_no("Would you like to include an advanced character set (lowercase/uppercase/special symbols)?")
    use_custom_chars = ask_yes_no("Would you like to specify a custom character set?")
    custom_chars = input("Enter the custom characters: ") if use_custom_chars else None
    # password strength
    strength = ask_strength()
    # pronounceability
    pronounceable = ask_yes_no("Do you want a pronounceable password?")
    # generation
    password = pg.generate_password(length, use_advanced, strength, pronounceable, custom_chars)
    print("Your generated password is:", password)
    print("Estimated password entropy:", pg.calculate_entropy(password))

def ask_yes_no(question):
    return input(f"{question} (yes/no) ").lower() == 'yes'

def ask_strength():
    options = ['low', 'medium', 'high']
    while True:
        strength = input("Choose the password strength (low/medium/high): ").lower()
        if strength in options:
            return strength
        else:
            print("Invalid option. Please choose 'low', 'medium', or 'high'.")

if __name__ == "__main__":
    main()
