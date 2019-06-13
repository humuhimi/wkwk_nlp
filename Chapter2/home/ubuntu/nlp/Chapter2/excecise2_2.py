"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
# import re

# path = "hightemp.txt"
# lines = ''
# with open(path) as f:
#     for s_line in f:
#         s_line = re.sub(r'\t',' ',s_line,count=3)
#         lines += s_line

#     print(lines)


path = "hightemp.txt"
lines = ''
with open(path) as f:
    for s_line in f:
        s_line =  s_line.replace('\t',' ',3) # 再代入してあげないといけない　変換するだけで別のオブジェクト
        lines += s_line

    print(lines)

