my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) > 1:
    my_list.insert(0, my_list.pop())
print("my_list:", my_list)
