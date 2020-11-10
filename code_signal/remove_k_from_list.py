'''
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

    For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
    removeKFromList(l, k) = [1, 2, 4, 5];
    For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
    removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 105,
    -1000 ≤ element value ≤ 1000.

    [input] integer k

    An integer.

    Guaranteed constraints:
    -1000 ≤ k ≤ 1000.

    [output] linkedlist.integer
        Return l with all the values equal to k removed.

'''

# Singly-linked lists are already defined with this interface:


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    ll_list = ll_to_arr(l)
    # for i in ll_list:
    #     if i == k:
    #         ll_list.remove(i)
    ll_list = list(filter(k.__ne__, ll_list))
    new_ll = create_ll(ll_list)
    return new_ll

def create_ll(arr):
    nodes = [ListNode(i) for i in arr]

    head = nodes[0]
    for i in range(0, len(arr)-1):
        node = nodes[i]
        next_node = nodes[i + 1]
        node.next = next_node

    return head


def ll_to_arr(head):
    ll = []
    current = head
    while current is not None:
        ll.append(current.value)
        current = current.next
    return ll


if __name__ == '__main__':
    l, k = [3, 1, 2, 3, 4, 5], 3
    node_head = create_ll(l)
    node_head = removeKFromList(node_head, k)
    print(ll_to_arr(node_head))
