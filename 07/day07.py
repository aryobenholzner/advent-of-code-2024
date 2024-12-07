import itertools
from dataclasses import dataclass

@dataclass
class Equation:
    expected_result: int
    variables: list[int]

def read_input(path: str) -> list[Equation]:
    file = open(path)
    lines = file.readlines()
    file.close()
    equations = []
    for line in lines:
        parts = line.split(":")
        result = parts[0]
        variables = parts[1].strip().split(" ")
        equations.append(Equation(int(result), list(map(int ,variables))))
    return equations

def solve(path: str, allowed_operations: list[str]):
    equations = read_input(path)
    return sum(map(lambda eq: eq.expected_result, filter(lambda eq: solvable(eq, allowed_operations), equations)))

def solvable(eq: Equation, allowed_operations: list[str]) -> bool:
    blanks = eq.variables.__len__() -1
    permutations = list(itertools.product(allowed_operations, repeat = blanks))
    for permutation in permutations:
        if calculate(permutation, eq.variables) == eq.expected_result:
            return True

def calculate(permutation, variables: list[int]):
    result = variables[0]
    for i in range(variables.__len__() - 1):
        if permutation[i] == '+':
            result += variables[i+1]
        elif permutation[i] == '*':
            result *= variables[i+1]
        elif permutation[i] == '||':
            result = int(str(result) + str(variables[i+1]))
    return result

def solve_a(path) -> int:
    return solve(path, ['+', '*'])

def solve_b(path) -> int:
    return solve(path, ['+', '*', '||'])

if __name__ == '__main__':
    print(solve_a('input'))
    print(solve_b('input'))