class FindPoints():
    def dist(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
        return dis

    def Points(self, points):
        current_minimum = float('inf')
        min_p1 = -1
        min_p2 = -1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = self.dist(points[i], points[j])
                if dis < current_minimum:
                    min_p1 = i
                    min_p2 = j
                    current_minimum = dis
        return str(points[min_p1]).replace('(', ' ').replace(')', ' ') +';'+str(points[min_p2]).replace('(', ' ').replace(')', ' ')