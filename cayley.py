from typing import List

class CayleyTable:
    """Represents a Cayley table for a binary operation on a finite set."""

    def __init__(self, n: int, table: List[List[int]]):
        """
        Initialize with set size n and a n x n table.
        Table is a list of lists: table[i][j] = i * j.
        """
        if len(table) != n or any(len(row) != n for row in table):
            raise ValueError("Table must be n x n.")
        self.n = n
        self.table = table

    def is_closed(self) -> bool:
        """Check if the operation is closed: all results in 0..n-1."""
        for row in self.table:
            for elem in row:
                if not (0 <= elem < self.n):
                    return False
        return True

    def operate(self, a: int, b: int) -> int:
        """Return a * b from the table."""
        return self.table[a][b]