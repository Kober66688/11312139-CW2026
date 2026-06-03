import sys

# sys.stdin 會整行整行讀取，包含裡面的空白
for line in sys.stdin:
    # 這題不能用 .strip() 喔！因為結尾的換行符號 \n 我們要保留，而且如果句子結尾有空白會被刪掉
    if not line:
        continue
        
    ans = []
    # 逐字元檢查這一行的每一個字
    for char in line:
        # 如果是換行符號，就不減 7，直接保留
        if char == '\n':
            ans.append(char)
        else:
            # 將字元轉成 ASCII 數字，減去 7，再轉回字元
            new_char = chr(ord(char) - 7)
            ans.append(new_char)
            
    # 把解密後的字元清單組合成一個字串印出來
    # end="" 代表不要讓 print 自動在最尾巴幫我們多加換行，因為我們已經保留原本的 \n 了
    print("".join(ans), end="")
