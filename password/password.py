while True:
    password = ''
    password = input('Create a password. It must contain at least 3 numbers, one capital letter, 8 symbols: ')
    numbers = len([letter for letter in password if letter.isdigit()])
    capital_letters = len([letter for letter in password if letter.isupper()])

    if len(password) >= 8 and numbers >= 3 and capital_letters >= 1:
        print('This is a strong password.')
        break
    print('It is unreliable password. Try again.')
