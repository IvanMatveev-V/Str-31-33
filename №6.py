b = 10

k = 0
t = 0
import time
while b + k + t != 100:
    sum = 100 - b * 10
    
    k = 0
    
    sum_n = sum - k * 5
    
    while b + k + t != 100 and sum_n > 0:
        k += 1
        
        sum_n = sum - k * 5
        t = sum_n // 0.5     
        
    if b + k + t != 100:
        b -= 1
    

print(b, k, t)
    