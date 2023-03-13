first = input('First line: ')
second = input('Second line: ')
print()


if len(first) == len(second) and first != second:
    for i in range (len(second)):
        second = second[1:] + second[0]
        if second == first:
            print('The first row can be obtained from the second by shifting the second by', i+1)
            break
        elif second != first and i == len (second)-1:
            print('The first row cannot be obtained from the second by a circular shift.')


elif first == second:
    print('The lines are identical.')

else:
    print('The first row cannot be obtained from the second.')