my_list = [1, 2, 3, 4, 5, 6]
index = 3
my_list_1 = my_list[:index]
my_list_2 = my_list[index:]
print(my_list_1, my_list_2)

my_list3 = [1, 2, 3]
index = 2
my_list3_1 = my_list3[:index]
my_list3_2 = my_list3[index:]
print(my_list3_1, my_list3_2)

empty_list = []
index = 2
empty_list1 = empty_list[:index]
empty_list2 = empty_list1[index:]
print(empty_list1, empty_list2)

new_list = [1, 2, 3, 4, 5]
index = 3
new_list1 = new_list[:index]
new_list2 = new_list[index:]
print(new_list1, new_list2)

my_list = [1, 2, 3, 4, 5, 6]
middle = len(my_list) // 2
list_1 = my_list[:middle]
list_2 = my_list[middle:]
print(list_1, list_2)

my_list = [1]
middle = len(my_list) // 2
list_1 = my_list[:middle]
list_2 = my_list[middle:]
print(list_1, list_2)
