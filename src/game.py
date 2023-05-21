import random
from abc import ABC, abstractmethod
from collections import Counter
from math import ceil
from typing import List, Tuple

from data import max_conns


class Tile(ABC):
    @property
    @abstractmethod
    def val(self):
        pass


class Digit(Tile):
    def __init__(self, val: int) -> None:
        if val <= 0:
            raise ValueError("Digit must have positive integer value")
        self._val = val

    @property
    def val(self):
        return self._val


class Empty(Tile):
    @property
    def val(self):
        raise ValueError("Empty tile has no value")


class DigitParty:
    digit_ratio = 9 / 25

    def __init__(self, n: int, digits: List[int] | None) -> None:
        self.n = n
        self.board: List[List[Tile]] = [[Empty() for _ in range(n)] for _ in range(n)]
        self.max_num = ceil(self.digit_ratio * n * n)
        self.digits = (
            list(map(lambda d: Digit(d), digits))
            if digits
            else [Digit(random.randrange(1, self.max_num)) for _ in range(n * n)]
        )
        self.placements: List[Tuple[Tuple[int, int], Digit]] = []
        self.score = 0

    def theoretical_max_score(self) -> int:
        score = 0
        counts = Counter(self.digits)
        for d in counts:
            score += max_conns[counts[d]] * d.val
        return score

    def _check_range(self, r: int, c: int):
        if r < 0 or r >= self.n or c < 0 or c >= self.n:
            raise ValueError(f"Row {r} or column {c} outside of board of size {self.n}")

    def place(self, r: int, c: int):
        self._check_range(r, c)
        if self.board[r][c]:
            raise ValueError(
                f"Board already contains tile {self.board[r][c].val} at row {r} column {c}"
            )
        d = self.digits.pop()
        self.board[r][c] = d
        self.placements.append(
            (
                (
                    r,
                    c,
                ),
                d,
            )
        )

        for dr, dc in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, -1),
        ]:
            try:
                self._check_range(r + dr, c + dc)
                if self.board[r + dr][c + dc] == d:
                    self.score += d.val
            except ValueError:
                continue

    def finished(self):
        return not self.digits and len(self.placements) == self.n * self.n
