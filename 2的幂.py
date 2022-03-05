class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        # 一般做法
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1
        '''

        '''
        # 位运算
        if n <= 0:
            return False
        return n & (n - 1) == 0
        '''

        # 二进制计数
        return bin(n).count('1') == 1 if n > 0 else False

n = 9
s = Solution()
print(s.isPowerOfTwo(n))