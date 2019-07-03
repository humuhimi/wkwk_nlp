"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ
"""
import re

path_w1 = "result/col1.txt"
path_w2 = "result/col2.txt"
path_f1_2 = "result/col1_2ans.txt"
combined_line = []

with open(path_w1, "r") as w1, open(path_w2, "r") as w2:
    for _w1, _w2 in zip(w1, w2):
        combined_line.append(_w1.rstrip("\r\n") + "\t" + _w2)

print("".join(combined_line))


with open(path_f1_2, "w") as res:
    for w in combined_line:
        res.write(w)
