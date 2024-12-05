from functools import cmp_to_key

def solve_a(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    delimiter_idx = lines.index("\n")
    lines = list(map(lambda line: str(line).removesuffix("\n"), lines))
    rules = list(map(lambda line: tuple(str(line).split('|')), lines[:delimiter_idx]))
    updates = lines[delimiter_idx+1:]
    return sum(map(find_middle, (filter(lambda update: update_correct(update, rules), updates))))

def update_correct(update: str, rules: list[tuple[str, ...]]) -> bool:
    pages = update.split(',')
    for i, page in enumerate(pages):
        page_rules = list(filter(lambda rule: tuple(rule)[0] == page, rules))
        for page_rule in page_rules:
            try:
                second_idx = pages.index(page_rule[1])
                if i > second_idx:
                    return False
            except ValueError:
                continue
    return True

def find_middle(line: str) -> int:
    values = list(map(lambda l: int(l), line.split(',')))
    return values[len(values)//2]


precedence = {}

def solve_b(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    delimiter_idx = lines.index("\n")
    lines = list(map(lambda line: str(line).removesuffix("\n"), lines))
    rules = list(map(lambda line: tuple(str(line).split('|')), lines[:delimiter_idx]))
    for left, right in rules:
        precedence.setdefault(left, set()).add(right)
    updates = lines[delimiter_idx+1:]
    to_order = list(filter(lambda update: not update_correct(update, rules), updates))

    return sum(map(lambda update: find_middle(order(update)), to_order))



def order(update: str) -> str:
    pages = update.split(',')
    return ','.join(sorted(pages, key=cmp_to_key(compare)))

def compare(x, y):
    if y in precedence.get(x, set()):
        return -1
    elif x in precedence.get(y, set()):
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(solve_a('input'))
    print(solve_b('input'))