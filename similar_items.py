
def similar_items(list1, list2):
    
    similar_items_list = [

    ]
    for item in list1:
        if item in list2 and item not in similar_items_list: 

            similar_items_list.append(item)
    return similar_items_list

   
result = similar_items([1,2,2,3], [2,3])

print(result)