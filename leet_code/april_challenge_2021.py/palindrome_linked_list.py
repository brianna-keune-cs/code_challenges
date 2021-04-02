'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp_arr = []

        current_node = head
        while current_node.next != None:
            temp_arr.append(current_node.val)
            current_node = current_node.next
        
        if temp_arr == temp_arr[::-1]:
            return True

if __name__ == '__main__':
    solution = Solution()
    ex1 = {"input": [1,2,2,1], "output": True}
    ex2 = {"input": [1,2], "output": False}
    
    print(solution.isPalindrome(ex1["input"]))
    print(solution.isPalindrome(ex2["input"]))
