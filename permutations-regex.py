import re
import itertools

char_list = ["m", "a", "m", "", "!"]

#find all permtations of a character list.
permutations_object = itertools.permutations(char_list)
permutations_list = list(permutations_object)
#print(permutations_list)


for list_obj in permutations_list:
    listToStr = '|'.join([str(elem) for elem in list_obj])
    m = re.findall(r'(^m+)', listToStr, re.IGNORECASE)
    print(listToStr,":", m)
