def selection_sort(my_list):
    for i_mn in range (len(my_list)):
        for curr in range (i_mn, len (my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


numbers_list = []
n = int(input('Enter the number of list items: '))

for i in range (n):
    number = int(input('Enter a list item: '))
    numbers_list.append(number)

selection_sort (numbers_list)
print(numbers_list)