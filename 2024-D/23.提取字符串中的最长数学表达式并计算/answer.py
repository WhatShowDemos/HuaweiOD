import re
 
def evaluate_expression(expression):
    """功能：计算简单数学表达式的值"""
    if not expression:
        return 0  # 如果表达式为空，返回 0
 
    values = []  # 使用栈来存储中间结果
    current_number = 0  # 当前解析的数字
    sign = '+'  # 当前数字前的操作符，默认为 '+'
    expression += '+'  # 在表达式末尾追加 '+'
    for c in expression:
        if c.isdigit():  # 如果字符是数字
            current_number = current_number * 10 + int(c)  # 累加形成整数
        elif c in '+-*':  # 如果字符是操作符
            if sign == '+':
                values.append(current_number)
            elif sign == '-':
                values.append(-current_number)
            elif sign == '*':
                values[-1] *= current_number
            current_number = 0  # 重置当前数字
            sign = c  # 更新操作符
 
    return sum(values)  # 返回计算结果
 
def find_and_evaluate(s):
    """功能：提取最长的合法数学表达式并计算其值"""
    exp_regex = re.compile(r"(\d+)([+*-]\d+)*")
    matches = exp_regex.finditer(s)
 
    longest_valid_expression = ""
    max_length = 0
 
    for match in matches:
        match_str = match.group()
        if len(match_str) > max_length and re.search(r"^(-?\d+([+*-]\d+)+)$", match_str):
            max_length = len(match_str)
            longest_valid_expression = match_str
 
    if not longest_valid_expression:
        return 0  # 如果没有合法表达式，返回 0
    else:
        return evaluate_expression(longest_valid_expression)  # 计算并返回表达式的值
 
def main():
    input_expr = input()
    result = find_and_evaluate(input_expr)
    print( result)
 
if __name__ == "__main__":
    main()