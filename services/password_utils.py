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
