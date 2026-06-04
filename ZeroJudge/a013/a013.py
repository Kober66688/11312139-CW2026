import sys

# 1. 羅馬數字轉阿拉伯數字的函式
def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        # 如果當前字元代表的值小於右邊字元代表的值，則減去當前值
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total

# 2. 阿拉伯數字轉回羅馬數字的函式
def int_to_roman(num):
    if num == 0:
        return "ZERO"
        
    # 將所有包含特殊減法規則的對應依序排列（由大到小）
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for value, symbol in val_map:
        while num >= value:
            result.append(symbol)
            num -= value
            
    return "".join(result)

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "#" or not line:
            break
            
        parts = line.split()
        if len(parts) < 2:
            continue
            
        # 讀入兩個羅馬數字並轉換為整數
        num1 = roman_to_int(parts[0])
        num2 = roman_to_int(parts[1])
        
        # 計算兩數之差的絕對值
        diff = abs(num1 - num2)
        
        # 將結果轉換回羅馬數字（或 ZERO）輸出
        print(int_to_roman(diff))

if __name__ == '__main__':
    main()
