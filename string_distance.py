from fuzzywuzzy import fuzz

def string_distance(list_of_strings, target_string):
    result = {}
    for item in list_of_strings:
        similarity = fuzz.ratio(item, target_string)
        result[item] = similarity
    return result

