def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    current_max = numbers[0]
    for num in numbers:
        if numbers[num] > current_max:
            current_max = numbers[num]
            
    return current_max

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
