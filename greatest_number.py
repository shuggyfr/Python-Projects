
def largest_number(number_list):
    largest = number_list[0]

    for number in number_list:
        if number > largest:
            largest = number

    return largest

number_list = [1,2,3]
print(largest_number(number_list))