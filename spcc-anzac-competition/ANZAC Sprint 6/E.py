a = input().split('/')
a[0] = int(a[0])
a[1] = int(a[1])

num = a[0]/a[1]

b = [1]
nodes = 1
total = 0

if (num < 1):
    if (a[0] + 1 == a[1]):
        b.append(a[0])
        nodes += a[0]
        total = a[1]
    else:
        print('impossible')
else:
    pass

node_num = 2
connects = []
nodeset = [1]
for level in range(1, len(b)):
    for i in range(b[level]):
        connects.append(f'{nodeset[level - 1]} {node_num}')
        if (len(nodeset) < level + 1):
            nodeset.append(node_num)
        node_num += 1

print(f'{nodes} {nodes - 1}')

for i in connects:
    print(i)
