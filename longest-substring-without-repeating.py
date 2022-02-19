# This solution has a O(n + n) = O(n) time complexity and O(n) space complexity
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    letters = []
    max_count = window_start = 0
    for end_letter in s:
        if(end_letter in letters):
            letters = letters[letters.index(end_letter) + 1:]
            window_start+=1
        letters.append(end_letter)
        max_count = max(max_count, len(letters))
    return max_count


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
    print("------------------------")
    print(lengthOfLongestSubstring("pwwkew"))
