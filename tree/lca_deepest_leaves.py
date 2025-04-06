from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Search:
    def dfs(self, node):
        if not node:
            return None, 0
        
        left_lca, left_depth = self.dfs(node.left)
        right_lca, right_depth = self.dfs(node.right)
        
        if left_depth == right_depth:
            return node, left_depth + 1
        elif left_depth > right_depth:
            return left_lca, left_depth + 1
        else:
            return right_lca, right_depth + 1
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest, _ = self.dfs(root)
        return deepest
        

tree = TreeNode(4)

tree.right = TreeNode(3)
tree.right.right = TreeNode(10)
tree.right.right.right = TreeNode(13)
tree.right.right.left = TreeNode(12)

tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(8)
tree.left.right.right = TreeNode(6)
tree.left.right.left = TreeNode(5)
tree.left.right.left.left = TreeNode(0)
tree.left.right.left.right = TreeNode(15)

search = Search()
deepest_leaves = search.lcaDeepestLeaves(root=tree)