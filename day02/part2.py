import argparse
from typing import List
from functools import reduce

import pytest


def compute(s: str) -> int:
    # import pdb; pdb.set_trace()
    total = 0
    for dim in s.strip().split('\n'):
        dim = list(map(int, dim.split('x')))
        dim.sort()
        total += 2*(dim[0]+dim[1])
        total += reduce(lambda x,y:x*y, dim, 1)
    return total

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('2x3x4', 34),
        ('1x1x10', 14),
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

