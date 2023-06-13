#!/usr/bin/env python3
even_list = []

def return_evens(num_list):
    for num in num_list:
        if num %2 == 0:
            even_list.append(num)
    return even_list

exclamation_list = []
def make_exclamation(sentence_list):
    for sentence in sentence_list:
        exclamation_list.append(sentence + "!")
    return exclamation_list