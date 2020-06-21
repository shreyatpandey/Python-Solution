"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
Approach - 1: Without using deque
Runtime:- 66.75%
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        Queue = []
        NaryTreeLevelOrderTraversal = []
        if not root:
            return NaryTreeLevelOrderTraversal
        level = 0
        Queue.append(root)
        while len(Queue) != 0:
            NaryTreeLevelOrderTraversal.append([])
            LenQueue = len(Queue)
            i = 0
            while i < LenQueue :
                node = Queue[0]
                del Queue[0]
                NaryTreeLevelOrderTraversal[level].append(node.val)
                if node.children :
                    Queue += node.children
                i += 1
            level += 1
        return NaryTreeLevelOrderTraversal
        
                        
