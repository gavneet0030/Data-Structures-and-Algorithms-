# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(left, right):
            if left > right:
                return [None]

            result = []

            for root in range(left, right + 1):
                left_trees = build(left, root - 1)
                right_trees = build(root + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        result.append(node)

            return result

        return build(1, n)