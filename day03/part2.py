import argparse
from typing import List

import pytest


def compute(s: str) -> int:
    santas_pos = [(0,0), (0,0)]
    visited = set()
    visited.add(santas_pos[0])
    visited.add(santas_pos[1])
    start = 0
    for m in s:
        pos = santas_pos[start]
        if m == '>':
            pos = (pos[0]+1, pos[1])
        elif m == '<':
            pos = (pos[0]-1, pos[1])
        elif m == '^':
            pos = (pos[0], pos[1]-1)
        elif m == 'v':
            pos = (pos[0], pos[1]+1)
        if pos not in visited:
            visited.add(pos)
        santas_pos[start] = pos
        if start == 1:
            start = 0
        elif start == 0:
            start = 1
    return len(visited)

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('^v', 3),
        ('^>v<', 3),
        ('^v^v^v^v^v', 11),
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

