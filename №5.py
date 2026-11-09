k = 0

while k < 17:
    g = 64
    
    for i in range(k):
        g -= 4
    
    print(f"Комбинация {k + 1}: {(64 - g) // 4} кроликов и {g // 2} гусей")
    
    
    k += 1