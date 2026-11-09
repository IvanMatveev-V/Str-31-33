for x in range(0, 29):
    f = 2 * (x ** 2) + 29
    
    u = True
    
    for i in range(2, f):
        if f % i == 0:
            u = False
        
    if u: print(f)