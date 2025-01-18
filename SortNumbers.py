max_num = int(input('How many numbers do you want to sort? '))
sort_choice = str(input('How do you want to sort? Type A for ascending and D for descending order: '))

num_list = []

if sort_choice == 'A' or sort_choice == 'D':
    for i in range(1, max_num+1):
        number = int(input(f'Enter number {i}: '))
        num_list.append(number)
else:
    print('You have not made a valid choice')

sorted_list = []
len_num = len(num_list)

while len(sorted_list) < len_num:
    if sort_choice == 'A':
        sorted_list.append(min(num_list))
        num_list.remove(min(num_list))
    
    else:
        sorted_list.append(max(num_list))
        num_list.remove(max(num_list))

if len(sorted_list) > 0:
    print(sorted_list)


