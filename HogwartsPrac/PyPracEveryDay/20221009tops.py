"""
 编写一个函数，该函数接受消息字符串并从最高到最低返回字符串的本地顶部。

字符串顶部是通过以下方式显示字符串：

                                                      3
                              p                     2   4
            g               o   q                 1
  b       f   h           n       r             z
a   c   e       i       m          s          y
      d           j   l             t       x
                    k                 u   w
                                        v

下一个顶部总是比上一个高1个字符。对于上面的示例，abcdefghijklmnopqrstuvwxyz1234输入字符串的解决方案是3pgb。

当消息字符串为空时，返回一个空字符串。
输入字符串可能很长。确保您的解决方案具有良好的性能。

题目难度：简单
题目来源： String tops | Codewars 7

def tops(msg:str) -> str:
    # your code here
    return ""

assert tops("") == ""
assert tops("12") == "2"
assert tops("abcdefghijklmnopqrstuvwxyz12345") == "3pgb"
assert tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN") == "M3pgb"
"""


def tops(msg: str) -> str:
    # 通过数学计算，可以得出第n个顶部值所在的位置为：2 * (n ** 2) - n + 1
    # 索引从0开始（需要减1），所以第n个顶部值所在的索引位置为：2 * (n ** 2) - n
    if msg == "":  # 当消息字符串为空时，返回一个空字符串
        return ""
    else:
        top_num_list = []
        for n in range(1, len(msg)):
            top_msg_index = 2 * (n ** 2) - n
            if top_msg_index >= len(msg):  # 当最后一个顶部值所在的索引位置 大于 字符长度，则退出循环
                break
            top_num_list.append(msg[top_msg_index])  # 获得字符串的顶部值，并按倒序排序
        top_num_list.reverse()
        return "".join(top_num_list)  # 列表格式转成字符串格式

    assert tops("") == ""
    assert tops("12") == "2"
    assert tops("abcdefghijklmnopqrstuvwxyz12345") == "3pgb"
    assert tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN") == "M3pgb"
