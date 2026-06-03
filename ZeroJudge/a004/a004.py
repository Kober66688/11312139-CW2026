import sys

# sys.stdin 完美符合題目要求的「一直讀到 EOF 結束」
for line in sys.stdin:
    if not line.strip():
        continue
        
    # 將輸入的年份轉換成整數
    year = int(line.strip())
    
    # 按照提示的規則進行邏輯判斷
    # % 4 == 0 代表被 4 整除； != 0 代表不被整除
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("閏年")
    else:
        print("平年")
