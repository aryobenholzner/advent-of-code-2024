
def solve_a(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    left = []
    right = []
    for line in lines:
        chars = line.split()
        left.append(int(chars[0]))
        right.append(int(chars[1]))
    left.sort()
    right.sort()
    distances = []
    for i, e in enumerate(left):
        distances.append(abs(e - right[i]))
    return sum(distances)

def solve_b(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    left = []
    right = []
    for line in lines:
        chars = line.split()
        left.append(int(chars[0]))
        right.append(int(chars[1]))
    similarity = 0
    for number in left:
        occurrences = right.count(number)
        similarity += (number * occurrences)
    return similarity

if __name__ == '__main__':
    print(solve_a('test_data'))
    print(solve_b('test_data'))