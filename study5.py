# 题5. 编写程序，把一个英文句子中的单词倒置，标点符号不倒置，例如 I like beijing. 经过函数后变为：beijing. like I

sentence = input("请输入一句英文：")
lst = sentence.split(' ')
lst.reverse()
ans = ' '.join(lst)
print(ans)