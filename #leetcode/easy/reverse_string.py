# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         y = []
#         for i in s:
#             y.append(i)
#         s = y[::-1]
#         print(s)

# s = "hello"
# sol1 = Solution()
# sol1.reverseString(s)

# 2nd Method-------------------------------------------------------
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Reverse the input list of characters in place.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage
s = ['a', 'n', 'k', 'i', 't']
sol = Solution()
sol.reverseString(s)
print(s)  # Output should be ['t', 'i', 'k', 'n', 'a']
