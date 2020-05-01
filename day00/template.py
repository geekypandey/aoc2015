import argparse
from typing import List

import pytest


def compute(s: str) -> int:
    # Implement solution here!
    return 0

@pytest.mark.parametrize(
    ('input_l', 'expected'),
    (
        # put the given test cases here
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

