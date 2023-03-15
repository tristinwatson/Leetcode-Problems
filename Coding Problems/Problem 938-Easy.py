# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        self.ans = 0

        def searchTree(root):
            if root:
                if root.val > low:
                    searchTree(root.left)
                if low <= root.val <= high:
                    self.ans += root.val
                if root.val < high:
                    searchTree(root.right)

        searchTree(root)
        return self.ans