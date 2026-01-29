def percentage_less_or_equal(list_of_num):
    # Create an empty dictionary to store each number and its percentage
    percentage_dictionary = {}
    # Get unique numbers from the list and sort them to remove duplicates
    each_number = sorted(set(list_of_num))

    total_of_numbers = len(list_of_num)

    # Loop through each unique number
    for number in each_number:
        # Initialize a counter for numbers less than or equal to the current number
        count = 0

        # Loop through the original list
        for numbers in list_of_num:
            # Check if the current number is less than or equal to 'number'
            if numbers <= number:
                count += 1

        # Calculate the percentage of numbers less than or equal to 'number'
        percentage = (count / total_of_numbers) * 100

        # Store the percentage in the dictionary with 'number' as the key
        percentage_dictionary[number] = percentage

    # Return the dictionary containing the results
    return percentage_dictionary

print(percentage_less_or_equal([3,1,2,3,4,2]))
