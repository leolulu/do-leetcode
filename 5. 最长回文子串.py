class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        result = dict()
        sota_result = 0
        for outb in range(length):
            if sota_result > length - outb:
                break
            for inb in range(outb, length):
                temps = s[outb:inb+1]
                if temps == temps[::-1]:
                    result[temps] = len(temps)
                    sota_result = max(sota_result, len(temps))
        return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]


s = Solution()
print(s.longestPalindrome('aabbbabababbabababb'))
