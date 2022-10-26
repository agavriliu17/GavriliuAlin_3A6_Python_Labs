#  Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because they can contain other 
# containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(first_dict, second_dict):

    if first_dict.keys() != second_dict.keys():
        return False

    for key in first_dict.keys():
        if type(first_dict[key]) == dict:
            if not compare_dicts(first_dict[key], second_dict[key]):
                return False

        elif type(first_dict[key]) == tuple or type(first_dict[key]) == set:
            if not compare_dicts(dict.fromkeys(first_dict[key]), dict.fromkeys(second_dict[key])):
                return False
                
        else:
            if first_dict[key] != second_dict[key]:
                return False
    return True

def main():
    first_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'e': 4,
            'f': 5,
            'g': 6,
            'h': {
                'i': 7,
                'j': 8,
            }
        }
    }

    second_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'e': 4,
            'f': 5,
            'g': 6,
            'h': {
                'i': 7,
                'j': 8,
                'k': 9,
                'l': {
                    'm': 10,
                    'n': 11,
                    'o': 12,
                }
            }
        }
    }

    print(compare_dicts(first_dict, second_dict))

main()