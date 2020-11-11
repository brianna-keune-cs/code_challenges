"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?


Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads - 121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # anything less than zero, will return false
        if (x < 0): 
            return False
        
        # if I convert the int to a string, we would just have to reverse it, convert back to a int, and compare to x

        x_str = list(str(x))
        x_str.reverse()
        
        x_reversed = int(''.join(x_str))

        return x == x_reversed


if __name__ == '__main__':
    solution = Solution()
  
    ex1 = [121, True]
    ex2 = [-121, False]
    ex3 = [10, False]
    ex4 = [-101,False]

    print(f'\ninput: {ex1[0]},\noutput: {ex1[1]} ,\n**result: {solution.isPalindrome(ex1[0])}**')

    print(
        f'\ninput: {ex2[0]},\noutput: {ex2[1]} ,\n**result: {solution.isPalindrome(ex2[0])}**')

    print(
        f'\ninput: {ex3[0]},\noutput: {ex3[1]} ,\n**result: {solution.isPalindrome(ex3[0])}**')

    print(
        f'\ninput: {ex4[0]},\noutput: {ex4[1]} ,\n**result: {solution.isPalindrome(ex4[0])}**')

