# 1519. Number of Nodes in the Sub-Tree With the Same Label

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        paths = defaultdict(list)
        result = [0] * n

        for e1, e2 in edges:
            paths[e1].append(e2)
            paths[e2].append(e1)

        def dfs(node, parent):
            nonlocal result
            cnt = Counter()
            for p in paths[node]:
                if p != parent:
                    cnt += dfs(p, node)
            cnt[labels[node]] += 1
            result[node] = cnt[labels[node]]
            return cnt

        dfs(0, -1)
        return result
