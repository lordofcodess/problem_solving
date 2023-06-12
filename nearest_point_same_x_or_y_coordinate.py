class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = float('inf')
        min_ind = -1

        for i, point in enumerate(points):
            px, py = point[0], point[1]
            if px == x or py == y:  
                dis = abs(px - x) + abs(py - y) 
                if dis < min_dis: 
                    min_dis = dis
                    min_ind = i

        return min_ind
