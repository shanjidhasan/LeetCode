# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_values(root, leaves):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
            get_leaf_values(root.left, leaves)
            get_leaf_values(root.right, leaves)

        leaves1 = []
        leaves2 = []

        get_leaf_values(root1, leaves1)
        get_leaf_values(root2, leaves2)

        return leaves1 == leaves2
