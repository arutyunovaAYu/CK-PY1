# TODO решить с помощью list comprehension и распечатать его

import pprint as pp

list_numbers = [i for i in range(0, 16)]
func = ["bin", "dec", "hex", "oct"]

empty_list = [{func[0]: bin(i), func[1]: i, func[2]: hex(i), func[3]: oct(i)} for i in list_numbers]

pp.pprint(empty_list)
