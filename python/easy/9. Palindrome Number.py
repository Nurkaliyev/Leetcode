class Solution:
    # 9. Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        # Special case: negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the number to a string and check if the string is the same forwards and backwards
        return str(x) == str(x)[::-1]