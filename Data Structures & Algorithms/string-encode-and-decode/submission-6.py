class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)%9) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        currWord = ""
        i = 0

        while i < len(s):
            if i < len(s) - 1 and s[i].isdigit() and s[i+1] == "#":
                if i != 0: # first one 
                    res.append(currWord)
                currWord = ""
                i += 1 # skip the # too
            else:
                currWord += s[i]
            i += 1
        if len(s) > 0:
            res.append(currWord)
        return res
