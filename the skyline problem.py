class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        bs = []
        for l, r, h in buildings:
            bs.append([l, h, 1])
            bs.append([r, h, 0])
        bs.sort(key=lambda b: (b[0], -b[1] if b[2] == 1 else b[1], -b[2]))

        res = []
        prev_height = 0 
        prev_x = -1
        active_buildings = []

        for x, h, is_left in bs:
            if is_left:
                bisect.insort(active_buildings, h)
            else:
                active_buildings.remove(h)

            skyline_height = active_buildings[-1] if active_buildings else 0
            if prev_height != skyline_height and prev_x != x:
                res.append([x, skyline_height])
                prev_height = skyline_height
                prev_x = x

        return res