"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

a = 'パタトクカシーー'
b = '' # 最初に変数を設定してないとデータが溜まっていくだけ
lists = []
for t in range(len(a)):
    lists.append(a[t])

for i in range(1,9,2):
    b += str(lists[i])

print(b)
