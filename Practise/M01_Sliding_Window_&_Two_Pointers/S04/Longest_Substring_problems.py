'''
#3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_length = 0
    char_index_map = {}
    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
s="abcabcbb"
print(lengthOfLongestSubstring(s))
'''














 
















