# 947. Most Stones Removed with Same Row or Column

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x = defaultdict(list)
        y = defaultdict(list)
        for coords in stones:
            x[coords[0]].append(coords[1])
            y[coords[1]].append(coords[0])
        
        connected = 0
        visited = set()
        
        for xx,yy in stones:
            q = deque()
            q.append((xx,yy))
            if (xx, yy) not in visited:
                connected += 1
            while q:
                px, py = q.popleft()
                if (px, py) not in visited:
                    visited.add((px, py))
                    for y_list in x[px]:
                        if py != y_list:
                            q.append((px, y_list))
                    for x_list in y[py]:
                        if px != x_list:
                            q.append((x_list, py))
        return len(stones) - connected