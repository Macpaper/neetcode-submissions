class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        currMax = -float('inf')
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                nIndex, nHeight = stack.pop()
                currMax = max(currMax, (i - nIndex) * nHeight)
                start = nIndex
            stack.append((start, heights[i]))
        while stack:
            nIndex, nHeight = stack.pop()
            currMax = max(currMax, (len(heights) - nIndex) * nHeight)
        return currMax