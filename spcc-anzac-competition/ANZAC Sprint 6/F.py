t1 = [int(x) for x in input().strip().split(" ")]
t2 = [int(x) for x in input().strip().split(" ")]

t1 = sorted(t1)
t2 = sorted(t2)

hyp1 = max(t1)
hyp2 = max(t2)

if t1 == t2:
    chyp1 = t1[0] ** 2 + t1[1] ** 2
    if t1[2] == chyp1 ** (0.5):
        print("YES")
    else:
        print("NO")
    
else:
    print("NO")