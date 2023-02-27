class Solution:
    # 394. Decode String
    def decodeString(self, s: str) -> str:
        k = 0  # Initialize the repetition factor to zero
        current_string = ''  # Initialize the current string to an empty string
        stack = []  # Initialize the stack to an empty list

        for char in s:  # Iterate through each character in the input string
            if char.isdigit():  # If the character is a digit, update the repetition factor
                k = k * 10 + int(char)
            elif char.isalpha():  # If the character is a letter, add it to the current string
                current_string += char
            elif char == '[':  # If the character is an opening bracket, push the current string and repetition factor onto the stack
                stack.append((current_string, k))
                k = 0  # Reset the repetition factor to zero
                current_string = ''  # Reset the current string to an empty string
            elif char == ']':  # If the character is a closing bracket, pop the top tuple from the stack and update the current string
                last_char, last_k = stack.pop(-1)
                current_string = last_char + last_k * current_string

        return current_string  # Return the decoded string
