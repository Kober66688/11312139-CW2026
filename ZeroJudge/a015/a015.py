import sys

def solve():
    # 使用 sys.stdin.read().split() 一口氣讀入所有被空白或換行隔開的字串
    # 這能完美應付題目提示中「測資檔包含多組矩陣資料」的狀況
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    while True:
        try:
            # 每次迴圈先讀取目前矩陣的列數 R 和行數 C
            R = int(next(iterator))
            C = int(next(iterator))
            
            # 依序讀取接下來的 R * C 個數字，並組合成二維清單（矩陣）
            matrix = []
            for _ in range(R):
                row = [int(next(iterator)) for _ in range(C)]
                matrix.append(row)
                
            # 利用 zip(*matrix) 進行轉置，把原本橫的列打包成直的行
            flipped_matrix = list(zip(*matrix))
            
            # 逐列印出翻轉後的矩陣內容，* 號可以直接將清單拆開並以空白隔開輸出
            for row in flipped_matrix:
                print(*row)
                
        except StopIteration:
            # 當所有測資都讀取完畢時，會觸發這個異常，此時安全退出迴圈
            break

if __name__ == '__main__':
    solve()
