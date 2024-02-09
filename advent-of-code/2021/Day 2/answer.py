text = open("input.txt", "r").readlines()

x = 0
y = 0

for line in text:
    direction, dist = line.split(" ")
    if direction == 'forward':
        x += dist
    elif direction == 'down':
        y += dist
    elif direction == 'up':
        y -= dist
    
print(x * y)

    

