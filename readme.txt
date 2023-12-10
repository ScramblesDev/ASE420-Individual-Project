# Advanced Password Generator

## Overview
The Advanced Password Generator is a Python-based application designed to create secure and customizable passwords. It offers a variety of features including setting password length, strength, pronounceability, and the use of custom character sets. Additionally, it calculates and displays the entropy of the generated password.

## Features
- **Password Length Customization**: Allows users to define the length of the generated password.
- **Strength Selection**: Users can select the strength (low, medium, high) of the password based on the desired level of randomness.
- **Pronounceability**: Option to generate pronounceable passwords using a Markov chain algorithm.
- **Entropy Calculation**: Displays the estimated entropy of the generated password, indicating its security level.
- **Custom Character Sets**: Users can specify custom characters for password generation.

## Installation
To use the Advanced Password Generator, follow these steps:
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the cloned directory.
3. Run the program using Python: `python program.py`

## Usage
Upon launching the program, follow the on-screen prompts to specify your preferences for the password:
1. Enter the desired password length.
2. Choose whether to include an advanced character set.
3. Specify the strength of the password (low, medium, high).
4. Decide if you want a pronounceable password.
5. If using a custom character set, enter the characters.

## Main Project Structure
- `program.py`: The entry point of the application.
- `/src`:
  - `markov_chain.py`: Handles the generation of pronounceable passwords.
  - `password_generator.py`: Core logic for password generation.
  - `password_utils.py`: Utility functions for user input and validation.
  - `password_validator.py`: Validates the generated passwords.

## Dependencies
- Python 3.x