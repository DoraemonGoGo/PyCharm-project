# 题1. 任意输入三个英文单词，按字典顺序输出。

t = input('请输入三个英文字母，并用逗号隔开：')
x, y, z = t.split(',')
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)
