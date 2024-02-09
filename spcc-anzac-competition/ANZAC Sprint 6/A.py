import math

H, _, b, a = [int(x) for x in input().strip().split(" ")]
print(- (((H * math.sqrt(a * b)) - (H * b))/(b - a)))