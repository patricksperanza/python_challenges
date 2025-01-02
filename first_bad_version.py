def first_bad(n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if is_bad_version():
            right = mid
        else:
            left = mid + 1
    return left


def is_bad_version():
    return True
