class Solution(object):
    # 递归
    '''def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)

        return False'''
    # 迭代
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        for i in 2, 3, 5:
            while n % i == 0:
                n = n // i
        return n == 1

n = 17
s = Solution()
print(s.isUgly(n))