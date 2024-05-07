class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        roman_value = {"i": 1,"v": 5,"x": 10, "l":50, "c":100, "d":500, "m":1000}
        arabic = 0
        prev_value = 0
        for i in reversed(s):
            value = roman_value[i]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
        return arabic

s = input("Enter a roman number: ").lower()
sol = Solution()
print(sol.romanToInt(s))
