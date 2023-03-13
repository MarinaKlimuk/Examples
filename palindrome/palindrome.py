def is_poly(string):
    char_dict = {}
    for symbol in string:
        char_dict[symbol] = char_dict.get(symbol, 0) + 1

    odd_count = 0
    for i in char_dict.values():
        if i % 2 != 0:
            odd_count += 1
    return odd_count <= 1


string_to_test = input('Enter the string: ')
if is_poly(string_to_test):
    print('A string can be turned into a palindrome_2')
else:
    print("A string can't be turned into a palindrome_2")