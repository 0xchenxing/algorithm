from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        sCounter = Counter()
        NSCounter = len(tCounter)
        left, right = 0, 0
        minLen = len(s)
        ans = ""
        while right < len(s):
            c = s[right]
            if c in tCounter:
                sCounter[c] += 1
                if sCounter[c] == tCounter[c]:
                    NSCounter -= 1
                if NSCounter == 0:
                    while left < right:
                        c = s[left]
                        if c not in tCounter:
                            left += 1
                        elif sCounter[c] > tCounter[c]:
                            left += 1
                            sCounter[c] -= 1
                        else:
                            break
                    if right - left + 1 <= minLen:
                        minLen = right - left + 1
                        ans = s[left:right+1]
            right += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
