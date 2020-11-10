'''
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
    checkPalindrome(inputString) = true.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A non-empty string consisting of lowercase characters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 105.

    [output] boolean
        true if inputString is a palindrome, false otherwise.

'''

def checkPalindrome(inputString):
    # print('str: ', inputString)
    # print('reversed: ', inputString[::-1])
    return True if inputString == inputString[::-1] else False


if __name__ == '__main__':
    inputString = "aabaa"
    print(f'{inputString} --> {checkPalindrome(inputString)}')

    inputString = "abac"
    print(f'{inputString} --> {checkPalindrome(inputString)}')
    
    inputString = "a"
    print(f'{inputString} --> {checkPalindrome(inputString)}')