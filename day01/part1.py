import argparse
from typing import List

import pytest


def compute(s: str) -> int:
    steps = list(s)
    floor = 0
    for step in steps:
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
    return floor

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('(())', 0),
        ('(()(()(', 3),
        (')())())', -3),
    ),
)
def test(input_s: List[int], expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())

