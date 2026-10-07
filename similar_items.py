
def similar_items(list1, list2):
    
    similar_items_list = []
    list2_lower = []

    for item in list2:
        list2_lower.append(item.lower())
        
    
    for item in list1:
        if item.lower() in list2_lower and item not in similar_items_list: 

            similar_items_list.append(item)
    return similar_items_list

   
result = similar_items(["dell", "kinder"], ["DELL", "Mac"])

print(result)