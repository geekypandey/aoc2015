import argparse
from typing import List

import pytest


def compute(s: str) -> int:
    steps = list(s)
    floor = 0
    for i,step in enumerate(steps):
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
    return floor

def compute_first(s: str) -> int:
    steps = list(s)
    floor = 0
    for i,step in enumerate(steps):
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
        if floor == -1:
            return i+1
    return 0

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('))(', 1),
    ),
)
def test(input_s: List[int], expected: int) -> None:
    assert compute_first(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute_first(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())

