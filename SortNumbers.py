while True:
    try:
        init_num = input('Paste the numbers you want to sort (separate with commas):  ')
        tup_num = tuple(map(int, init_num.split(",")))
        num_list = list(tup_num)
        while True:
            try:
                sort_choice = str(input('How do you want to sort? Type A for ascending and D for descending order: '))


                if sort_choice == 'A' or sort_choice == 'D' or sort_choice == 'a' or sort_choice == 'd':
                    sorted_list = []
                    len_num = len(num_list)
                    
                    while len(sorted_list) < len_num:
                        if sort_choice == 'A' or sort_choice == 'a':
                            sorted_list.append(min(num_list))
                            num_list.remove(min(num_list))
                        
                        else:
                            sorted_list.append(max(num_list))
                            num_list.remove(max(num_list))

                    if len(sorted_list) > 0:
                        print(sorted_list)
                
                else:
                    raise ValueError()
                
                break
            except ValueError:
                print("Invalid choice! Please choose A or D.")
        



        break
    
    except ValueError:
        print('You need to input only integers. Try again!')


