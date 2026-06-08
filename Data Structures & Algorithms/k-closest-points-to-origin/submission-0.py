class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 点key = 坐标， value = distance hashmap按value排序
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:k]
        