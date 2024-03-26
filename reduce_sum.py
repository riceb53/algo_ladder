def reduce_sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(reduce_sum([1,2,3,4]))