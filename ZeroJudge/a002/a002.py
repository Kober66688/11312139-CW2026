import sys

# 連續讀取多組測試資料
for line in sys.stdin:
    # 檢查這一行是不是空的（如果是空的就跳過，防止出錯）
    if not line.strip():
        continue
        
    # 用 split() 把一行裡面的多個數字切開
    # 例如 "5 10" 會變成 ["5", "10"]
    parts = line.split()
    
    # 將切開的文字轉換成整數 (int)
    a = int(parts[0])
    b = int(parts[1])
    
    # 算出總和並印出
    print(a + b)
