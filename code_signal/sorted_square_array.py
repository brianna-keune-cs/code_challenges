'''
Note: Come up with a linear solution, since that is what you would be asked to do in an interview.

You have a sorted array of integers. Write a function that returns a sorted array containing the squares of those integers.

Example

For array = [-6, -4, 1, 2, 3, 5], the output should be
sortedSquaredArray(array) = [1, 4, 9, 16, 25, 36].

The array of squared integers from array is: [36, 16, 1, 4, 9, 25]. When sorted, it becomes: [1, 4, 9, 16, 25, 36].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer array

    A sorted array of integers.

    Guaranteed constraints:
    1 ≤ array.length ≤ 104,
    -104 ≤ array[i] ≤ 104.

    [output] array.integer
        A sorted array of integers composed of the squared integers from the input array.

'''

def sortedSquaredArray(array):
    return sorted([i ** 2 for i in array])

if __name__ == '__main__':
    arr1 = [-6, -4, 1, 2, 3, 5]
    print(sortedSquaredArray(arr1))