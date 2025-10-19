from typing import Optional, Tuple
from cayley import CayleyTable

def is_associative(table: CayleyTable) -> bool:
    """Check associativity: (a*b)*c == a*(b*c) for all a,b,c."""
    n = table.n
    for a in range(n):
        for b in range(n):
            for c in range(n):
                ab = table.operate(a, b)
                bc = table.operate(b, c)
                if table.operate(ab, c) != table.operate(a, bc):
                    return False
    return True

def is_commutative(table: CayleyTable) -> bool:
    """Check commutativity: a*b == b*a for all a,b."""
    n = table.n
    for a in range(n):
        for b in range(n):
            if table.operate(a, b) != table.operate(b, a):
                return False
    return True

def find_neutral(table: CayleyTable) -> Optional[int]:
    """Find neutral element e if exists: a*e == e*a == a for all a."""
    n = table.n
    for e in range(n):
        if all(table.operate(a, e) == a for a in range(n)) and \
           all(table.operate(e, a) == a for a in range(n)):
            return e
    return None

def is_left_solvable(table: CayleyTable) -> bool:
    """Check left solvability: for all a,b exists x: a*x == b."""
    n = table.n
    for a in range(n):
        for b in range(n):
            if not any(table.operate(a, x) == b for x in range(n)):
                return False
    return True

def is_right_solvable(table: CayleyTable) -> bool:
    """Check right solvability: for all a,b exists y: y*a == b."""
    n = table.n
    for a in range(n):
        for b in range(n):
            if not any(table.operate(y, a) == b for y in range(n)):
                return False
    return True

def is_invertible(table: CayleyTable, neutral: Optional[int]) -> bool:
    """Check invertibility: each a has left/right inverse if neutral exists."""
    if neutral is None:
        return False
    n = table.n
    for a in range(n):
        has_left_inv = any(table.operate(x, a) == neutral for x in range(n))
        has_right_inv = any(table.operate(a, x) == neutral for x in range(n))
        if not (has_left_inv and has_right_inv):
            return False
    return True