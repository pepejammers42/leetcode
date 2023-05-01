"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs
        # if not node:
            # return node
        
        # q = deque()
        # q.append(node)
        # r = {node.val: Node(node.val)}

        # while q:
            # cur = q.popleft()
            
            # for n in cur.neighbors:
                # if n.val not in r:
                    # r[n.val] = Node(n.val)
                    # q.append(n)
                # r[cur.val].neighbors.append(r[n.val])

        # return r[node.val]
        
        # dfs
        d = {}
        
        def clone(node):
            if node.val in d:
                return d[node.val]
            cur = Node(node.val)
            d[node.val] = cur
            
            for n in node.neighbors:
                cur.neighbors.append(clone(n))
            return cur
        return clone(node) if node else None
