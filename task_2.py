main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_ = {}
def get_count_char(str_):
    str_ = "".join(main_str.split())
    str_ = str_.lower()
    str_list = list(str_)

    for i in str_list:
        if i.isalpha():
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
    print(dict_)
    return dict_

get_count_char(main_str)
new_dict = {}
def percent_dict(main_dict):
    count_ = sum(main_dict.values())
    for i in main_dict:
            new_dict[i] = round(dict_[i] * 100 / count_, 3)
    print(new_dict)
    return new_dict

percent_dict(dict_)