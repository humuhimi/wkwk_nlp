"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

N = int(input("出力したい行数を入力してください:"))

filepath = "col1_2ans.txt"
lines = []
rline = []

with open(filepath, "r") as f:
    for line in f:
        lines.append(line)
    for line_r in reversed(lines):
        if N > 0:
            rline.append(line_r)
        else:
            rline.reverse()
            break

        N -= 1

for r in rline:
    print(r)

"""
if n > 0:
    with open(path) as f:
        lines = f.readlines() # これを使うべきやった。
    for line in lines[-n:]:
        print(line.rstrip())
"""
