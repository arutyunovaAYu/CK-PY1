import random

def get_unique_list_numbers() -> list[int]:
    get_unique_list_numbers = []
    while len(get_unique_list_numbers) < 15:
        z = random.randrange(-10, 10)
        if z not in get_unique_list_numbers:
            get_unique_list_numbers.append(z)
    return(get_unique_list_numbers)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
