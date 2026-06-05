import sys

# 定義運算子的優先順序
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0

# 執行單步運算
def apply_op(operators, values):
    if len(values) < 2:
        return
    b = values.pop()
    a = values.pop()
    op = operators.pop()
    
    if op == '+': values.append(a + b)
    elif op == '-': values.append(a - b)
    elif op == '*': values.append(a * b)
    elif op == '/': 
        # 題目要求 C 語言定義的整除（向 0 靠攏截斷）
        # Python 的 // 是向下取整，在處理負數時會有差異，因此用 int(a / b) 最安全
        values.append(int(a / b))
    elif op == '%': values.append(a % b)

def evaluate(expression):
    # 將算式中的括號和運算子前後加上空格，方便用 split 切開
    for tokens in ['+', '-', '*', '/', '%', '(', ')']:
        expression = expression.replace(tokens, f' {tokens} ')
    
    tokens = expression.split()
    values = []
    operators = []
    
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_op(operators, values)
            if operators:
                operators.pop() # 彈出 '('
        elif token in ('+', '-', '*', '/', '%'):
            while operators and precedence(operators[-1]) >= precedence(token):
                apply_op(operators, values)
            operators.append(token)
            
    while operators:
        apply_op(operators, values)
        
    return values[0] if values else 0

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        print(evaluate(line))

if __name__ == '__main__':
    main()
