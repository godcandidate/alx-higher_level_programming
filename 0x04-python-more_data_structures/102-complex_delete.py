#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())

    for dic_value in dict_keys:
        if value == a_dictionary.get(dic_value):
            del a_dictionary[dic_value]

    return (a_dictionary)
