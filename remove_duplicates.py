def remove_duplicates(items):
    new_list = []

    for item in items:
        if item not in new_list:
            new_list.append(item)

    return new_list

result = remove_duplicates([1,2,2,3,4])

print(result)
