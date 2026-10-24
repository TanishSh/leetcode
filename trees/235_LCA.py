# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        root_val = root.val
        p_val = p.val
        q_val = q.val

        if root_val:
            left_node = root.left
            right_node = root.right

            if p_val < root_val and q_val < root_val:
                return self.lowestCommonAncestor(left_node, p, q)

            elif p_val > root_val and q_val > root_val:
                return self.lowestCommonAncestor(right_node, p, q)

            else:
                return root
        
        else:
            return root


        

        






        