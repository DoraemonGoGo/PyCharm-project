# 题6. 编写程序，递归删除指定文件夹中指定类型的文件。

from os.path import isdir, join, splitext
from os import remove, listdir

F = ['.txt']


def DF(x):
    for subPath in listdir(x):
        p = join(x, subPath)
        if isdir(p):
            DF(p)
        elif splitext(p)[1] in F:
            remove(p)


def main():
    x = r'F:\PyCharm'
    DF(x)


main()
