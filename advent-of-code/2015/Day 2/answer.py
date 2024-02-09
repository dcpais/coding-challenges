from utils import *

# -------------- Define Helper Functions Here
def sa(l, w, h):
    return 2 * l * w + 2 * l * h + 2 * w * h

# -------------- Main Entry Point
if __name__ == "__main__":
    rects = read_input("input.txt")
    total_area = 0
    total_ribbon = 0
    for rect in rects:
        dims = [int(x) for x in rect.split("x")]
        dims.sort()
        area = sa(*dims) + dims[0] * dims[1]
        total_area += area
        total_ribbon += 2 * dims[0] + 2 * dims[1]
        total_ribbon += dims[0] * dims[1] * dims[2]
        
    print(f"Total Surface Area: {total_area}")
    print(f"Total Ribbon length: {total_ribbon}")