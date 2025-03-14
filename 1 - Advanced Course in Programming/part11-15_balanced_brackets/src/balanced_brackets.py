
def balanced_brackets(my_string: str):
    filtered_string = "".join(c for c in my_string if c in "[]()")
    
    if len(filtered_string) == 0:
        return True

    valid_pairs = ["()", "[]"]

    for pair in valid_pairs:
        if pair in filtered_string:
            return balanced_brackets(filtered_string.replace(pair, "", 1))

    return filtered_string == ""
