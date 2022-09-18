def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - value

        if remaining in seen:
            return [i, seen[remaining]]
        else:
            seen[value] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

