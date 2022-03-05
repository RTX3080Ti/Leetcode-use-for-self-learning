'''
class Solution:
        def backtrack(参数):
            if 终止条件:
                保存结果
                return
            for 遍历：本层集合中的元素（树中节点孩子的数量）:
                #处理节点
                backtrack(路径，选择列表)  #递归
                #回溯，撤销处理的节点
'''

class Solution:
    def combine(self, n: int, k: int):
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n-(k-len(path))+2):  #剪枝
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res

s = Solution()
print(s.combine(4, 3))
