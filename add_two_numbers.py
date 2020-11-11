'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8F
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # we have to traverse each linked list,
        # and store their values into seperate integers
        # add up integers,
        # then create a linked list out of reverse order of list

        # idea 1:
        # traverse each linked list seperately,
        # store each val into a list,
        # reverse each list
        # make each list into a string,
        # string into integers,
        # add them up
        # change back into a string,
        # pop off values into list nodes
        # until the length of the list is 0.

        # turning linked list into array
        array1 = self.ll_to_array(l1)
        array2 = self.ll_to_array(l2)

        # make array's correct integers
        num1 = self.llarray_to_number(array1)
        num2 = self.llarray_to_number(array2)

        result = str(num1 + num2)
        list_nodes = []

        for num in result:
            new_node = ListNode(int(num))
            list_nodes.append(new_node)

        list_nodes.reverse()
        
        head = list_nodes[0]

        self.create_linked_list(list_nodes)

        return head

    def create_linked_list(self, arr):
        for i in range(0, len(arr)-1):
            node = arr[i]
            next_node = arr[i + 1]
            node.next = next_node

    def ll_to_array(self, head):
        result = []
        current = head

        while current is not None:
            result.append(current.val)
            current = current.next

        return result

    def llarray_to_number(self, arr):
        sum = 0

        for i in range(0, len(arr)):
            digits_place = 10 ** i
            num = arr[i]
            if i == 0:
                sum += num
            else:
                sum += num * digits_place

        return sum


if __name__ == '__main__':

    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1_head = ListNode(2)
    l1_next = ListNode(4)
    l1_next1 = ListNode(3)

    l1_head.next = l1_next
    l1_next.next = l1_next1

    l2_head = ListNode(5)
    l2_next = ListNode(6)
    l2_next1 = ListNode(4)

    l2_head.next = l2_next
    l2_next.next = l2_next1

    result = Solution()

    current = result.addTwoNumbers(l1_head, l2_head)

    linked_list = []
    while current is not None:
        linked_list.append(current.val)
        current = current.next

    print(linked_list)
