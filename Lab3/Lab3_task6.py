list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = max(list_numbers)
index_ = list_numbers.index(max_)

list_numbers[index_], list_numbers[-1] = list_numbers[-1], list_numbers[index_]

print(list_numbers)