class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        someNum = 0
        for n in nums:
            someNum = someNum ^ n
        return someNum