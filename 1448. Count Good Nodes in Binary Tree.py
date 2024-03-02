# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if node is None:
                return 0

            good_node_count = 1 if node.val >= max_val else 0

            max_val = max(max_val, node.val)

            left_count = dfs(node.left, max_val)
            right_count = dfs(node.right, max_val)

            return good_node_count + left_count + right_count

        return dfs(root, float('-inf'))
