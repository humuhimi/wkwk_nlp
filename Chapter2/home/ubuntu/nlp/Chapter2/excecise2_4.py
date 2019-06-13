"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ
"""
path_w1 = "col1.txt"
path_w2 = "col2.txt"
path_f1_2 = "col1_2ans.txt"
w1_line = []
w2_line = []

import re

with open(path_w1,'r') as w1:
    with open(path_w2,'r') as w2:
        for _w1 in w1:
            w1_line.append(_w1)
        for _w2 in w2:
            w2_line.append(_w2)


# print(w1_line[:]+w2_line[:])

for i in range(len(w1_line) - 1):
    w1_line[i] += w2_line[i]
    w1_line[i] = re.sub(r'\n','\t',w1_line[i],1)

print(w1_line)


with open(path_f1_2,'w') as res:
    for w in w1_line:
        res.write(w)
        
