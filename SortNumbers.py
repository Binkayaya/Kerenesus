sort_choice = str(input('How do you want to sort? Type A for ascending and D for descending order: '))


if sort_choice == 'A' or sort_choice == 'D':
    init_num = input('Paste the numbers you want to sort (separate with commas):  ')
    tup_num = tuple(map(int, init_num.split(",")))
    num_list = list(tup_num)
    
    
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
   
else:
    print('You have not made a valid choice')


