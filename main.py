# Add the import statements for functions from string_utils.py and equation_utils.py here
from string_utils import split_before_uppercases, split_at_digit
from equation_utils import (
    count_atoms_in_molecule,
    parse_chemical_reaction,
    count_atoms_in_reaction,
    build_equations
)

def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    raw = my_solve(equations, coefficients)

    # האחרון הוא ה־b האחרון (לפי build_equations החדש)
    last = raw[-1]

    normalized = [coef / last for coef in raw]

    return normalized

