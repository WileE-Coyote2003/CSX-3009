x = list(map(int, input().split()))

def max_crossing_sum(arr, left, mid, right):
    s = 0
    left_sum = float('-inf')
    for i in range(mid, left - 1, -1):
        s += arr[i]
        left_sum = max(left_sum, s)

    s = 0
    right_sum = float('-inf')
    for i in range(mid + 1, right + 1):
        s += arr[i]
        right_sum = max(right_sum, s)

    return left_sum + right_sum


def max_sub_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_sub_sum(arr, left, mid)
    right_max = max_sub_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)




print(max_sub_sum(x, 0, len(x) - 1))