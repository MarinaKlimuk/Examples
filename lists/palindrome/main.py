word = input('Enter a word: ')
symbol_list = list(word)
new_symbol_list = []

for i in range(1,len(symbol_list)+1):
    new_symbol_list.append(symbol_list[-i])


if symbol_list == new_symbol_list:
    print('The word is a palindrome')
else:
    print('The word is not a palindrome')