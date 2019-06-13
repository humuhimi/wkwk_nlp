"""
これは間違って作ったやつ
ファイルの分割数ではなく、ファイルの分割行
"""




import string

N = int(input('分割行数を入力してください:'))

a_Z = string.ascii_letters

path_I = "hightemp.txt"
path_O = "path_f_splited.txt"

lists = []

with open(path_I,'r') as I:
    for i in I:
        lists.append(i)


d = 0 # a-z用のインデックス

while len(lists) > 0:
    with open(path_O,'w') as O:
        for i in range(N):
            try: # ファイルに書き込み　リストからポップさせる
                O.write(lists[i])
                lists.pop(i)
            except:
                None
        else:
            d += 1
            print(d)  
            path_O = "path_f_splited.txt" + a_Z[d]
            




