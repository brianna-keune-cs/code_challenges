# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# what does it mean by a 32-bit signed integer range? https://www.quora.com/What-is-32-bit-signed-integer?share=1

# when do I return 0 -- when does the integer 'overflow'? 
# value limits:
# max: (2^31) - 1
# least: -(2^31)

# 31 being the max bits it can show a number, the 32th bit is for the sign.

# otherwise it looks like I am taking an integer, and reversing the places but not the sign

# in example 3, the zero that would be in the front was taken off, and in example 4 where there is a zero it returned zero. 

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

# Example 4:

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x):
        min_value = -(2**31)
        max_value = (2**31) - 1
        is_negative = False
       
        # check to make sure I recieved an integer
        if (isinstance(x, int) is False):
            return 0
        
        # seperate integer into an array
        int_list = list(str(x))

        if (int_list[0] == '-'):
            is_negative = True
            int_list.pop(0)

        # run array through loop, 
        # that pops off the end into a new list
        reversed = list()
        while len(int_list) > 0:
            moving_int = int_list.pop()
            reversed.append(moving_int)

        # loop through new list,
        # if the first int is 0, skip until it's not, create new int
        # return that int

        reversed_num = ''.join(reversed)
        reversed_int = int(reversed_num)
        


        if (min_value <= reversed_int <= max_value):
            if (is_negative == True):
                return reversed_int * -1
            return reversed_int
        return 0




if __name__ == '__main__':
    solution = Solution()

    print(f'Given the integer: 123, the result should be [321]\nresult: {solution.reverse(123)}')
    print(
        f'\nGiven the integer: -123, the result should be [-321]\nresult: {solution.reverse(-123)}')
    print(
        f'\nGiven the integer: 120, the result should be [21]\nresult: {solution.reverse(120)}')
    print(
        f'\nGiven the integer: 0, the result should be [0]\nresult: {solution.reverse(0)}')
