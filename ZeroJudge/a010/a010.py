import sys

for line in sys.stdin:
    if not line.strip():
        continue
        
    n = int(line.strip())
    
    factors = []  # 用來存放每個因數文字的清單（例如 ['2^2', '5']）
    i = 2
    
    # 開始短除法模擬
    while i * i <= n:
        count = 0
        # 如果能被 i 整除，就一直除，並計算次方
        while n % i == 0:
            count += 1
            n //= i
            
        # 如果有成功被除過，代表 i 是因數
        if count > 0:
            if count == 1:
                factors.append(str(i))
            else:
                factors.append(f"{i}^{count}")
        i += 1
        
    # 如果最後剩下的 n 大於 1，代表 n 本身也是一個質因數
    if n > 1:
        factors.append(str(n))
        
    # 用 " * " 把所有的因數文字串接起來印出
    print(" * ".join(factors))
