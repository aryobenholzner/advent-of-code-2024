import functools
import re


def solve_a(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    total_sum = 0
    for line in lines:
        total_sum += calc_line(line)
    return total_sum

def calc_line(line: str) -> int:
    results = re.findall('mul\((\d+),(\d+)\)', line)
    return sum(map(lambda t: int(t[0]) * int(t[1]), results))

def solve_b(path):
    file = open(path)
    line = file.read()
    file.close()
    line = line.replace("\n", "")
    dos = re.findall('(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)', line)
    return sum(map(calc_line, dos))


if __name__ == '__main__':
    print(solve_a('input'))
    print(solve_b('input'))