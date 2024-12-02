def solve_a(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    safe = 0
    for line in lines:
        nums = list(map(int, line.split()))
        sorted_nums = nums.copy()
        sorted_nums.sort()
        if nums == sorted_nums:
            for i, num in enumerate(nums):
                if i < nums.__len__() - 1:
                    next_num = int(nums[i+1])
                    diff = next_num - num
                    if 1 <= diff <= 3:
                        continue
                    else:
                        break
                else:
                    safe += 1
        sorted_nums.reverse()
        if nums == sorted_nums:
            for i, num in enumerate(nums):
                if i < nums.__len__() - 1:
                    next_num = int(nums[i+1])
                    diff = num - next_num
                    if 1 <= diff <= 3:
                        continue
                    else:
                        break
                else:
                    safe += 1
    return safe

def solve_b(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    safe = 0
    check_for_removal = []
    for line in lines:
        nums = list(map(int, line.split()))
        is_safe = line_safe(nums)
        if is_safe:
            safe += 1
        else:
            check_for_removal.append(nums)
    for e in check_for_removal:
        if check_with_removal(e):
            safe += 1
    return safe

def line_safe(nums) -> bool:
    asc = is_ascending(nums)
    if asc:
        return safe_with_tolerance(nums, asc)
    else:
        return safe_with_tolerance(nums, asc)

def is_ascending(nums: list[int]):
    return nums[0] < nums[nums.__len__() - 1]

def safe_with_tolerance(nums: list[int], asc: bool):
    iterator = iter(nums)
    _first = next(iterator)
    for i, num in enumerate(nums):
        next_num = next(iterator, -1)
        if next_num == -1:
            return True
        diff = calc_diff(num, next_num, asc)
        if 1 <= diff <= 3:
            continue
        return False

def check_with_removal(nums: list[int]):
    print(str(nums))
    for i in range(0, nums.__len__()):
        copy = nums.copy()
        copy.pop(i)
        if line_safe(copy):
            return True

def calc_diff(first: int, second: int, inverse: bool):
    if inverse:
        return second - first
    return first - second

if __name__ == '__main__':
    print(solve_a('test_data'))
    print(solve_b('test_data'))