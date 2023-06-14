#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    values = list(a_dictionary.items())
    best_scorer = values[0]
    for i in values:
        best_scorer = i if i[1] > best_scorer[1] else best_scorer

    return best_scorer[0]
