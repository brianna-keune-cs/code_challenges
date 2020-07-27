'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

 

Follow-up:
Can you solve it without using extra space?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # keeps track of nodes that have been visited
        visited = set()
        
        # keeps track of which node we are currently looking at
        current = head
        
        # traversing linked list, until we reach its tail
        while current is not None:
            
            # if current node is in visited, return node
            if current in visited:
                return current
            
            # else we add what we current to visited
            visited.add(current)
            # increment linked list counter
            current = current.next
        
        # if we reach tail of linked list without finding a match in visited
        # return None which is equal to null 
        return

if __name__ == '__main__':

    l1_head = ListNode(3)
    l1_next = ListNode(2)
    l1_next1 = ListNode(0)
    l1_next2 = ListNode(4)

    l1_head.next = l1_next
    l1_next.next = l1_next1
    l1_next1.next = l1_next2
    l1_next2.next = l1_next

    solution = Solution()

    print(solution.detectCycle(l1_head).val, "== should be 2")

