"""
编写一个函数，该函数接受一个括号字符串，并确定括号的顺序是否有效。如果字符串有效，则函数应返回true，如果字符串无效，则返回false。

示例
“()” => 真
“)(()))” => 假
“(” => 假
“(())((()())())” => 真

制约因素

0 <= 输入长度 <= 100

除了左括号 “(” 和右括号 “)” 之外，输入可以包含任何有效的ASCII字符。此外，输入字符串可能为空和/或根本不包含任何括号。不要将其他形式的括号视为括号（例如[ ]、{ }、< >）。

题目难度：一般
题目来源： Valid Parentheses | Codewars 2

def valid_parentheses(s: str) -> bool:
    #your code here
    return False

assert valid_parentheses("  (") == False
assert valid_parentheses(")test") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi())(") == False
assert valid_parentheses("hi(hi)()") == True
"""


def valid_parentheses(s: str) -> bool:
    num_i = 0
    for i in s:
        if i == "(":
            num_i += 1
        if i == ")":
            num_i -= 1
        if num_i < 0:  # 括号对出现以“）”开头的，括号的顺序无效，
            return False
    if num_i == 0:  # 出现成对的括号或没有括号，返回True
        return True
    else:  # 出现不成对的括号，返回False，如"  ("
        return False


assert valid_parentheses("  (") == False
assert valid_parentheses(")test") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi())(") == False
assert valid_parentheses("hi(hi)()") == True
