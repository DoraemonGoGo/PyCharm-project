# 题2. 编写程序，判断今天是今年的第几天。

import time

date = time.localtime()
y, m, d = date[:3]
t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print("今天是" + str(y) + "年" + str(m) + "月" + str(d) + "日")

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    t[1] = 29

if m == 1:
    print(d)

else:
    month = int(m)
    s = sum(t[:month - 1]) + d
    print("是今年的第" + str(s) + "天")