'''
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.storage.insert(0, x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        popped = self.storage.pop()
        return popped

    def peek(self):
        """
        Get the front element.
        """
        return self.storage[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if len(self.storage) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4, '  expect: 1, 2, false')
