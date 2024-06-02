class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        y = []
        for i in s:
            y.append(i)
        s = y[::-1]
        print(s)

s = "hello"
sol1 = Solution()
sol1.reverseString(s)