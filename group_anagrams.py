'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

'''


class Solution:
    def groupAnagrams(self, strs):
        # create a cache of letters in first word
        # will have to split up each word
        # check if in cache[key]'s set
        # if intersection of split is equal to length of set add word
        # else create a new key
        # words_cache = {}
        # letters_cache = list()
        # key_count = 0

        # for word in strs:
        #     letter_values = sorted(list(word))
        #     if word not in words_cache:
        #         words_cache[word] = letter_values
        #     if letter_values not in letters_cache:
        #         letters_cache.append(letter_values)
        #         key_count += 1
        # result = [[] * len(letters_cache)]

        # while len(words_cache.keys()) > 0:
        #   for word in strs:

        # # result[index].append(key)
        # return result

        cache = {}
        for word in strs:
          key = tuple(sorted(word))
          if key in cache:
            cache[key].append(word)
          else:
            cache[key] = [word]
        return cache.values()


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
          '\n\nexpected:\n[\n    ["ate","eat","tea"],\n    ["nat","tan"],\n    ["bat"]\n]')
