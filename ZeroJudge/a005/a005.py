import sys

def solve():
    # 讀取所有輸入並過濾掉空白行
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return
        
    # 第一行是測資組數，我們不需要特別用到它，因為後面直接用迴圈跑剩下的行數
    # 跑剩下的每一組數列
    for line in lines[1:]:
        # 把四個數字切開並轉成整數清單，例如 [1, 2, 3, 4]
        nums = [int(x) for x in line.split()]
        
        a, b, c, d = nums[0], nums[1], nums[2], nums[3]
        
        # 判斷是否為等差數列
        if (b - a) == (c - b):
            diff = b - a       # 算出公差
            e = d + diff       # 算出第五項
        else:
            ratio = b // a     # 算出公比（用 // 代表整除）
            e = d * ratio      # 算出第五項
            
        # 把第五項加進原本的清單中
        nums.append(e)
        
        # 按照題目要求，用空白隔開印出這五個數字
        # *(星號) 可以把清單拆開來印出，中間自動補空白
        print(*nums)

if __name__ == '__main__':
    solve()
