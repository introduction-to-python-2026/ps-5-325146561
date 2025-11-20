
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

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atoms = {}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        atoms[atom_name] = atoms.get(atom_name, 0) + atom_count

    # Step 3: Return the completed dictionary
    return atoms

