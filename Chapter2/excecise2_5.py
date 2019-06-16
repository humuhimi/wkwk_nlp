"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

N = int(input('出力したい行数を入力してください:'))

path = "hightemp.txt"

with open(path,'r') as f:
    for line in f:

        if N > 0:
            print(line)
        else:
            break   

        N -= 1
        
        