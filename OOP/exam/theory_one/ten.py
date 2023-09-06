import math
class construted_distict:
    def distinct(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

print("%.6f" % construted_distict().distinct(5, 2, 4, 3))
