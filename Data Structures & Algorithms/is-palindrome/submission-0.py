class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Create the alphanumeric string version
        s = ''.join(char.lower() for char in s if char.isalnum())

        # Initialzing the pointers
        left, right = 0, len(s) - 1

        while left < right:

            # if at some point the char at the right index != char at the right, return false
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        