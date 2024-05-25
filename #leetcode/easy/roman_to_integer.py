class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        roman_value = {"i": 1,"v": 5,"x": 10, "l":50, "c":100, "d":500, "m":1000}
        arabic = 0
        prev_value = 0
        for i in reversed(s):
            if i not in roman_value:
                return "Invalid Roman numeral"
            value = roman_value[i]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
                prev_value = value
        if 1 <= arabic and arabic <= 3999:
            return arabic

s = input("Enter a roman number: ").lower()
if 1 <= len(s) and len(s) <= 15:
    sol = Solution()
    print(sol.romanToInt(s))
else:
    print("Length of roman number should be more than 0 and less then 16 !!!")
