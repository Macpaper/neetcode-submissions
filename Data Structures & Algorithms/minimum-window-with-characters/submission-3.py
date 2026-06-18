class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        haveTotal = 0
        needTotal = len(t)
        have = {}
        need = {}
        minimum = s
        for letter in t:
            have[letter] = 0
            need[letter] = need.get(letter, 0) + 1
        l, r = 0, 0
        found = False
        while r < len(s):
            letter = s[r]
            if letter in need:
                have[letter] += 1
                if have[letter] <= need[letter]:
                    haveTotal += 1
            while haveTotal == needTotal:
                found = True
                if r - l + 1 < len(minimum):
                    minimum = s[l:r+1]
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        haveTotal -= 1

                l += 1
            r += 1

        if found:
            return minimum
        else:
            return ""