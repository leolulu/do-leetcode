import re


class Solution:
    patten = re.compile(r"\d\[[a-z]+\]")

    def decodeString(self, s: str) -> str:
        decode_string = ''
        find_pattens = re.findall(Solution.patten, s)
        if len(find_pattens) > 0:
            for find_patten in find_pattens:
                decode_string += self.decodeString(find_patten)
        else:
            decode_string += s
        return decode_string


if __name__ == "__main__":
    s = Solution()
    s.decodeString("3[a]2[bc]")
