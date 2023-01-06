class Solution:
    # 3. Longest Substring Without Repeating Characters
    # Version 1.
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to store characters in current substring
        char_set = set()
        # initialize max length
        max_len = 0
        # initialize start and end pointers
        start = 0
        end = 0
        # loop until end pointer reaches end of string
        while end < len(s):
            # if current character not in char_set
            if s[end] not in char_set:
                # add current character to char_set and update max_len if necessary
                char_set.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                # if current character is already in char_set, remove characters from start until current character is removed
                char_set.remove(s[start])
                start += 1
        # return max length
        return max_len

    # Version 2.
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # dictionary to store characters and their indices in current substring
    #     char_dict = {}
    #     # initialize max length
    #     max_len = 0
    #     # initialize start of current substring
    #     start = 0
    #     # loop through string
    #     for end, char in enumerate(s):
    #         # if char already in char_dict, update start to index of char + 1
    #         if char in char_dict:
    #             start = max(start, char_dict[char] + 1)
    #         # update char_dict with char and its index
    #         char_dict[char] = end
    #         # update max_len if necessary
    #         max_len = max(max_len, end - start + 1)
    #     # return max length
    #     return max_len