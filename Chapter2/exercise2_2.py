"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
filepath = "hightemp.txt"
lines = ""
with open(filepath) as f:
    for s_line in f:
        s_line = s_line.replace("\t", " ", 3)  # 再代入してあげないといけない　変換するだけで別のオブジェクト
        lines += s_line

    print(lines)
