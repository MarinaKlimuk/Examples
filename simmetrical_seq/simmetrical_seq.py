def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) -1,-1,-1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


new_nums = []
answer = []

N = int(input('How many numbers will be in the list: '))
nums = [int(input("Enter single number and press enter: ")) for _ in range(N)]


for i_nums in range(0,len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0,i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []


print('Original list:', nums)
print('How many numbers must be added to make a palindrome_2:', len(answer))
print ('List of these numbers:', answer)