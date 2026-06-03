import sys

# 連續讀取多組測試資料
for line in sys.stdin:
    if not line.strip():
        continue
        
    # 用 split() 把月和日切開，例如 "1 2" 變成 ["1", "2"]
    parts = line.split()
    
    M = int(parts[0])  # 月
    D = int(parts[1])  # 日
    
    # 套用題目給的公式算出生肖運勢的代號 S
    S = (M * 2 + D) % 3
    
    # 根據 S 的值判斷要印出什麼
    if S == 0:
        print("普通")
    elif S == 1:
        print("吉")
    elif S == 2:
        print("大吉")
