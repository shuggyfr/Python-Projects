def remove_duplicates(items):
    new_list = []

    for item in items:
        if item not in new_list:
            new_list.append(item)

    return new_list

result = remove_duplicates([1,2,2,3,4])

print(result)

# shortcut  I found - list(dict.fromkeys(items))

# reasoning : since dictionaries cannnot have duplicate keys,
# dict.fromkey(items) builds a dictionary using the items as the key and asssigns a none value
# then we use list() to turn it back to a list