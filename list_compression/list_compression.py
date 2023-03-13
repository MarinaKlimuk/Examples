import random

amount = int(input('How many numbers will be in the list: '))
expanded_list = [random.randint(0,2) for _ in range(amount)]
print('List before compression:', expanded_list)
expanded_list.sort(key=lambda x: not x)
print('Sorted list:',expanded_list)
compressed_list = [x for x in expanded_list if x]
print('Compressed list:', compressed_list)