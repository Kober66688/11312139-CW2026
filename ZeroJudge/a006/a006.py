import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue
        
    # 讀入 a, b, c 三個整數
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    
    # 計算判別式 D = b^2 - 4ac
    D = b**2 - 4*a*c
    
    # 情況 1：兩個相異實根
    if D > 0:
        # math.isqrt() 可以直接求出整數開根號，非常方便
        sqrt_D = math.isqrt(D)
        x1 = (-b + sqrt_D) // (2 * a)
        x2 = (-b - sqrt_D) // (2 * a)
        print(f"Two different roots x1={x1} , x2={x2}")
        
    # 情況 2：重根
    elif D == 0:
        x = -b // (2 * a)
        print(f"Two same roots x={x}")
        
    # 情況 3：無實根
    else:
        print("No real root")
