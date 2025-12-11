def merge_lists(list1, list2, condition='common'):
    if condition == 'common':
        
        return list(set(list1) & set(list2))
    elif condition == 'unique':

        return list((set(list1) | set(list2)) - (set(list1) & set(list2)))
    elif condition == 'all':

        return list(set(list1) | set(list2))
    else:
        raise ValueError("Неверное условие. Допустимо: 'common', 'unique', 'all'")



list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(merge_lists(list1, list2, 'common'))  
print(merge_lists(list1, list2, 'unique')) 
print(merge_lists(list1, list2, 'all'))     
