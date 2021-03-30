'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def twoSum(self, nums, target):
        # brute force
        # nested loops, will probably time out.
        # for j in range(0, len(nums) - 1):
        #     for k in range(0, len(nums) - 1):
        #         num1, num2 = nums[j], nums[k + 1]
        #         if j is k + 1:
        #             continue
        #         elif num1 + num2 == target:
        #             return [j, k + 1]

        # idea 2:
        # input: list of nums, target num
        # output, list, of indexes that sum up to target
        # we loop through list,
        # create a cache of numbers, and what number will get to target
        # when target is found, return those indexes

        # ~~~~~~~~~~~ WORKING ~~~~~~~~~~~~~~~~~
        # naive?
        # cache = {}
        # location = []

        # # creating cache
        # for index, num in enumerate(nums):
        #     if index not in cache:
        #         cache[(index, num)] = target - num

        # # finding possible solutions in cache
        # for key, num in cache.items():
        #     index, value = key
        #     temp = None
        #     if num in nums:
        #         location.append(index)

        # print('location: ', location)
        # if len(location) == 2:
        #     index1, index2 = location[0], location[1]
        #     if nums[index1] + nums[index2] == target:
        #         return location

        # # searching for two indexes that sum equal to target
        # for j in range(0, len(location) - 1):
        #     for k in range(0, len(location) - 1):
        #         index1, index2 = location[j], location[k + 1]
        #         num1, num2 = nums[index1], nums[index2]
        #         if j is k + 1:
        #             continue
        #         elif num1 + num2 == target:
        #             return [index1, index2]
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # second pass
        # runtime: O(n)
        # space: O(n)
        cache = {}

        # create cache of num at index
        # num is in target (complement of target)
        for index, num in enumerate(nums):
            cache[num] = index
        
        # loop through nums list
        for i in range(len(nums)):
            # compare value at index in nums to complement of target
            complement = target - nums[i]
            # if complement is in cache
            # and that complement is not at the same index (so we do not use the same element twice)
            if complement in cache and cache[complement] != i:
                # return location indexes
                return [cache[complement], i]


solution = Solution()
print(solution.twoSum([-1, -2, -3, -4, -5], -8))
