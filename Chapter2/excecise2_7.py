"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import string

a_Z = string.ascii_letters
d = 0


N = int(input('分割ファイル数を入力してください:'))
path_I = "hightemp.txt"
path_O = "path_f_splited.txt"
lists = []

with open(path_I,'r') as I:
    for i in I:
        lists.append(i)


split_n = len(lists)//N # split_n ずつ持ってきたらいい

while len(lists) > 0:
    with open(path_O,'w') as O:
        try:
            for j in range(split_n):
                O.write(lists[j])
                lists.pop(j)
            else:
                if len(lists) <= split_n:
                    continue
                else:
                    path_O = "path_f_splited.txt" + a_Z[d]
                    d += 1
        except:
            print('終了')


    






