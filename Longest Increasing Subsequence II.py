class SegmentTree:
    def __init__(self, n, fn):
        self.n = n
        self.fn = fn
        self.tree = [0] * (2 * n)
       
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                res = self.fn(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.fn(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:    
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        res = 1
        tree = SegmentTree(n, max)
        for num in nums:
            num -= 1
            mm = tree.query(max(0, num - k), num)
            tree.update(num, mm + 1)
            res = max(res, mm + 1)
        return res