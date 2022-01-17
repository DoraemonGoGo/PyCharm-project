import math

x = input('请输入两边长及夹角：\n')
a, b, c = map(float, x.split())
print('第三边长为：')
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(c / 180 * math.pi)))
