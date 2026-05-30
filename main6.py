import random
original_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
new_list = [original_list[0], original_list[2], original_list[-2]]
print("first_list:", original_list)
print("result (new_list):", new_list)