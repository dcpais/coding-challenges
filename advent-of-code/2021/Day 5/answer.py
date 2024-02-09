from utils import *

class Line:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2 

    def get_line_coords(self):
        dx = self._point1[0] - self._point2[0]
        dy = self._point1[1] - self._point2[1]
        steps = max(abs(self._point1[0] - self._point2[0]), \
            abs(self._point1[1] - self._point2[1]))

        coords = []
        mx = dx / steps
        my = dy / steps
        for i in range(steps + 1):
            coords.append((int(self._point2[0] + (i * mx)), \
                 int(self._point2[1] + (i * my))))
        return coords

    def is_straight(self):
        return (self._point1[0] - self._point2[0] == 0) or \
            (self._point1[1] - self._point2[1] == 0)

    def __repr__(self):
        return f"{point1} -> {point2}"


def get_coord_count(lines: List[Line], straightOnly: bool) -> int:
    
    coordCount = dict()
    for line in lines:
        if line.is_straight() and straightOnly:
            continue
        lineCoords = line.get_line_coords()
        for coord in lineCoords:
            count = coordCount.get(coord)
            if count is None:
                coordCount[coord] = 1
            else:
                coordCount[coord] += 1
                    

    countTwoAtleast = 0
    for count in coordCount.values():
        if count >= 2:
            countTwoAtleast += 1

    return countTwoAtleast


if __name__ == '__main__':
    data = read_input("input.txt")
    lines = []

    #Store all line segments in list
    for item in data:
        temp = item.split(" -> ")
        point1 = tuple([int(x) for x in temp[0].split(",")])
        point2 = tuple([int(x) for x in temp[1].split(",")])
        lines.append(Line(point1, point2))

    #Part 1: straight lines only
    stepOne = get_coord_count(lines, True)
    print(f"Part 1: count of intersections is {stepOne}")

    #Part 2: all lines
    stepTwo = get_coord_count(lines, False)
    print(f"Part 2: count of intersections is {stepTwo}")

    
    
        
    

    


