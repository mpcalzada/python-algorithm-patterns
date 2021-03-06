
# This solution has a O(n) time complexity and O(n) space complexity because of the HashMap
def twoSumWithHash(nums, target):
    pairs = {}
    for i, val1 in enumerate(nums):
        val2 = target - val1
        if val2 in pairs:
            return [pairs[val2], i]
        else:
            pairs[val1] = i


# This solution has a O(n) time complexity and O(1) space complexity because of the HashMap
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    p2 = len(nums) - 1
    p1 = 0
    for i in nums:
        current_sum = nums[p1] + nums[p2]
        print(f"{nums[p1]} + {nums[p2]} = {current_sum}")
        if (current_sum > target and target > 0) or (current_sum < target and target < 0):
            p2 -= 1
        elif (current_sum < target and target > 0) or (current_sum > target and target < 0):
            p1 += 1
        else:
            return[p1, p2]
    return [p1, p2]


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([-1, -2, -3, -4, -5], -8))
    print(twoSum([-10, 7, 19, 15], 9))
