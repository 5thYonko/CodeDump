n = [9, 8, 72, 22, 21, 81, 2, 1, 11, 76, 32, 54]

def highest(n):
    for i in n:
        highest = 0
        if i > n[i+1]:
            i = highest
        elif n[i+1]> i[n]:
            n[i+1] = highest
 

print(highest)



