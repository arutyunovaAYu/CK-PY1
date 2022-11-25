import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        #создаем json строку:
        json_string = []
        #заполняем её: #enumerate - счетчик элементов
        #number - номер строки
        for number, line in enumerate(f):
            #получаем значения в каждой строке - values_ с разделителем ","
            values_ = line.strip(new_line).split(delimiter)
            #если номер строки - 0, то это "column"
            if number == 0:
                headers = values_
                continue
            #получаем отдельные строки json
            json_string.append({})
            for j, _ in enumerate(headers):
                json_string[-1][headers[j]] = values_[j]
        return json_string

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))