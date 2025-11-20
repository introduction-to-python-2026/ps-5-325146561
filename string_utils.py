
def split_before_uppercases(formula): 
    if formula == "":
        return []
    
    parts = []
    current = formula[0]

    for char in formula[1:]:
        if char.isupper():
            parts.append(current)
            current = char
        else:
            current += char

    parts.append(current)
    return parts

def split_at_digit(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number


