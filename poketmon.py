def solution(nums):
    nums_set = len(set(nums))
    length = len(nums) // 2

    if nums_set < length:
        return nums_set
    else:
        return length
print(solution([3,1,2,3]))
