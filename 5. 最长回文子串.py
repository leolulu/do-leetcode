class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        result = dict()
        for outb in range(length):
            for inb in range(outb, length):
                temps = s[outb:inb+1]
                if temps == temps[::-1]:
                    result[temps] = len(temps)
        return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]


s = Solution()
print(s.longestPalindrome('aa'))
