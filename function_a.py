def most_common_value(number_list):
    """ returns the most common element of the list
    """

    current_num = number_list[0]
    count = 0

    for num in number_list:

        if number_list[num] != current_num:

            current_num = number_list[num]
            count = 1
        
        elif number_list[num] == current_num:
            count += 1
    
    return current_num


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
