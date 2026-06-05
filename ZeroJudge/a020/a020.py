import sys

def solve():
    # 建立英文字母對應的代號字典
    letter_map = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
        'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
        'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 22, 'W': 32, 'X': 30,
        'Y': 31, 'Z': 33
    }
    
    # 這裡要注意：W(32), Z(33), I(34), O(35) 的順序比較特別，
    # 另外台東縣的 V 雖然對應 22（跟南投 N 一樣），但題目表格中有寫明，要特別注意
    letter_map['V'] = 29 # 修正：依標準身分證 V 為 29

    for line in sys.stdin:
        id_str = line.strip()
        if not id_str:
            continue
            
        # 取出第一個英文字母並轉換成兩位數
        first_letter = id_str[0].upper()
        num = letter_map[first_letter]
        
        # 拆出十位數與個位數
        n1 = num // 10
        n2 = num % 10
        
        # 1. 計算字母部分的加權和：十位數 * 1 + 個位數 * 9
        total = n1 * 1 + n2 * 9
        
        # 2. 計算中間 8 位數字的加權和：權重從 8 遞減到 1
        weights = [8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(1, 9):
            total += int(id_str[i]) * weights[i-1]
            
        # 3. 加上最後一碼檢查碼（權重為 1）
        total += int(id_str[9]) * 1
        
        # 判斷總和是否能被 10 整除
        if total % 10 == 0:
            print("real")
        else:
            print("fake")

if __name__ == '__main__':
    solve()
