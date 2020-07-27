'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

class Solution:
    def containsDuplicate(self, nums):
        # idea 1: 
            # use nested loops,
            # outer loop, would hold onto the value we're checking
            # inner loop, would loop through list against checking value
            # if match, return true,
            # else increment to next index
            
        # idea 2:
            # create a cache, or a 'memory', maybe using a set
            # to hold previously seen values
            # if current value through a loop through list is found in visited list
            # return true, else false.
            
            seen_values = set()
            
            for i in nums:
                if i in seen_values:
                    return True
                
                seen_values.add(i)
                
            return False

if __name__ == '__main__':
    solution = Solution()
    print(f'result: {solution.containsDuplicate([1,2,3,1])} should be True')
    print(f'\nresult: {solution.containsDuplicate([1,2,3,4])} should be False')