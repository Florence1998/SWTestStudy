"""
 ISBN-10标识符的长度为十位数。前九个字符是数字0-9。最后一个数字可以是0-9或X，表示值为10。

如果数字之和乘以其位置模11等于零，则ISBN-10数字有效。

例如:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
它是一个合法的ISBN-10 :

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
例子
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
题目难度：简单
题目来源： ISBN-10 Validation | Codewars 5

def valid_ISBN10(isbn: str) -> bool:
    # your code here

assert valid_ISBN10('1112223339') ==True
assert valid_ISBN10('048665088X') == True
assert valid_ISBN10('1293000000') == True
assert valid_ISBN10('1234554321') == True
assert valid_ISBN10('1234512345') == False
assert valid_ISBN10('1293') == False
assert valid_ISBN10('X123456788') == False
assert valid_ISBN10('ABCDEFGHIJ') == False
assert valid_ISBN10('XXXXXXXXXX') == False
assert valid_ISBN10('123456789T') == False
assert valid_ISBN10('048665088XX') == False
"""


def valid_ISBN10(isbn: str) -> bool:
    isbn_len = len(isbn)
    num_sum = 0
    if isbn_len != 10:  # 判断标识符的长度是否为十位数，不是则返回False
        return False
    else:               # 以下为标识符的长度为十位数的情况
        num_index = 1
        for num_value in isbn:
            if num_index < 10:  # 判断前九个字符是数字0-9，不是则返回False
                if num_value not in "0123456789":
                    return False
                    break
            if num_index == 10:  # 判断第十个数字是0-9或X，不是则返回False
                if num_value not in "0123456789X":
                    return False
                    break
                if num_value == "X":  # X表示值为10
                    num_value = 10
            num_sum += int(num_value) * num_index
            num_index += 1
    if num_sum % 11 == 0:  # 数字之和乘以其位置模11等于零，则ISBN-10数字有效，返回True，否则，返回False
        return True
    else:
        return False


assert valid_ISBN10('1112223339') == True
assert valid_ISBN10('048665088X') == True
assert valid_ISBN10('1293000000') == True
assert valid_ISBN10('1234554321') == True
assert valid_ISBN10('1234512345') == False
assert valid_ISBN10('1293') == False
assert valid_ISBN10('X123456788') == False
assert valid_ISBN10('ABCDEFGHIJ') == False
assert valid_ISBN10('XXXXXXXXXX') == False
assert valid_ISBN10('123456789T') == False
assert valid_ISBN10('048665088XX') == False
