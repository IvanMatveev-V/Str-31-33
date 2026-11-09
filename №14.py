A = int(input())
B = int(input())

s = 0

for i in range(10):
    s += B - A
    
    B *= 1.03
    
print(s)