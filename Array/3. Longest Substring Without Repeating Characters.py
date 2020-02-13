class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        cur_str = set()
        cur_len = 0
        max_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in cur_str:
                cur_str.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            cur_str.add(s[i])
        return max_len