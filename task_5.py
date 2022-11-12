import random
def get_random_password() -> str:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ALPHABET =[i.upper() for i in alphabet]
    numbers_list = [i for i in range(0, 9)]

    grand_alphabet = alphabet + ALPHABET + numbers_list

    my_password = random.sample(grand_alphabet, 8)

    my_new_pass = ''.join(map(str, my_password))

    return my_new_pass

print(get_random_password())
