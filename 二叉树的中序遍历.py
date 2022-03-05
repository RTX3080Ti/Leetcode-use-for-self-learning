# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	def inorderTraversal(self, root: TreeNode):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		def dfs(root):
			if not root:
				return

			dfs(root.left)
			res.append(root.val)
			dfs(root.right)
		dfs(root)
		return res

root = [1,None,2,3]
s = Solution()
print(s.inorderTraversal(root))