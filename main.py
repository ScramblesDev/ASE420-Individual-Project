import password_generator as pg

def main():
    print("Welcome to the Password Generator!")
    length = int(input("How long would you like the password to be? "))
    use_advanced = input("Would you like to include advanced character sets (lowercase/uppercase/special symbols)? (yes/no) ").lower()
    strength = input("How strong would you like the password to be (high/medium/low randomness)? ").lower()
    pronounceable = input("Do you want pronounceable passwords? (yes/no) ").lower()

    # generates the password
    password = pg.generate_password(length, use_advanced == 'yes', strength, pronounceable == 'yes')
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
