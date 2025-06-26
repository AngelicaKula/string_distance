#Angelica Kula
#AngelicaKula
#2025-25-06
#Description: A function that takes two arguments and returns a dictionary
from fuzzywuzzy import fuzz

def string_distance(list_of_strings, target_string):
    "Calculates the Levenshtein distance between two strings."
    result = {}
    for item in list_of_strings:
        similarity = fuzz.ratio(item, target_string) #Compute similarity
        result[item] = similarity #Store result in dictionary
    return result

#---Test Function---
my_list_of_strings = ["A", "B", "C", "D", "E", "F"]
target_string = "A"

#---Print Result---
result = string_distance(my_list_of_strings, target_string)
print(result)

