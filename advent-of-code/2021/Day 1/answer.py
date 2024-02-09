text = open("input.txt", "r").readlines()

x = 0
y = 0
aim = 0

for line in text:
    direction, dist = line.split(" ")
    dist = int(dist)
    if direction == 'forward':
        x += dist
        y += aim * dist
    elif direction == 'down':
        aim += dist
    elif direction == 'up':
        aim -= dist
    
print(x * y)

    

