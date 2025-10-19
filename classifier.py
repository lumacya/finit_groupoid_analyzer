from properties import (
    is_associative, is_commutative, find_neutral,
    is_left_solvable, is_right_solvable, is_invertible
)
from cayley import CayleyTable

def classify(table: CayleyTable) -> list[str]:
    """
    Classify the structure based on properties.
    Returns a list of applicable classifications.
    """
    classifications = []
    
    closed = table.is_closed()
    associative = is_associative(table)
    commutative = is_commutative(table)
    neutral = find_neutral(table)
    left_solvable = is_left_solvable(table)
    right_solvable = is_right_solvable(table)
    invertible = is_invertible(table, neutral) if neutral is not None else False
    
    if closed and associative:
        classifications.append("Полугруппа (Semigroup)")
    if closed and left_solvable and right_solvable:
        classifications.append("Квазигруппа (Quasigroup)")
    if closed and associative and neutral is not None:
        classifications.append("Моноид (Monoid)")
    if closed and left_solvable and right_solvable and neutral is not None:
        classifications.append("Лупа (Loop)")
    if closed and associative and left_solvable and right_solvable and neutral is not None and invertible:
        classifications.append("Группа (Group)")
    if closed and associative and left_solvable and right_solvable and neutral is not None and invertible and commutative:
        classifications.append("Абелева группа (Abelian Group)")
    
    return classifications