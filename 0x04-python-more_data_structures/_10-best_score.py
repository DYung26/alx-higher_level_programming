#!/usr/bin/python3
def best_score(a_dictionary):
    sVal = sorted({v for v in a_dictionary.values() if v is not None})
    n_dictionary = {}
    for key, value in a_dictionary.items():
        for sVals in sVal:
            if a_dictionary[f'{key}'] == sVals:
                n_dictionary.update({key: sVals})
