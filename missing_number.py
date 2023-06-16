def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2

    for num in nums:
        expected_sum -= num

    return expected_sum
