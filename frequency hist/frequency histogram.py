
def histogram (string):
    sym_dict = dict()
    for symbol in string:
        if symbol in sym_dict:
            sym_dict[symbol] += 1
        else:
            sym_dict[symbol] = 1
    return sym_dict

def inverted_dict(symbol_dict):
    number_dict = dict()
    for symbol in symbol_dict:
        number = symbol_dict[symbol]
        if number in number_dict:
            number_dict[number].append(symbol)
        else:
            number_dict[number] = [symbol]


    return number_dict


text = input('Enter the text: ').lower()
hist = histogram(text)

print('Original frequency dictionary: ')
for symbol in sorted(hist.keys()):
    print(symbol,':',hist[symbol])

inverted_hist = inverted_dict(hist)

print()
print('Inverted frequency dictionary:')
for element in inverted_hist:
    print(element,':',inverted_hist[element])



