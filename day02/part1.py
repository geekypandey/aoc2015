import argparse
from typing import List

import pytest


def compute(s: str) -> int:
    # import pdb; pdb.set_trace()
    total = 0
    for dim in s.strip().split('\n'):
        l, w, h = map(int, dim.split('x'))
        area = 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
        total += area
    return total

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('2x3x4', 58),
        ('1x1x10', 43),
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

