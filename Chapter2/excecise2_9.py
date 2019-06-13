"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

def reverse_list(path):
        path_i = path
        with open(path_i,'r') as I:
            for i in I:
                lists.append(i)
        for j in lists[::-1]:
            print(j)




# lists =  make_list(path_I)
# sort_target = []

# for line in lists:
#         line = line.split('\t')
#         sort_target.append(line[2])
#         print(line[2])
# else:
#     print(sort_target)

if __name__ == '__main__':
    
    path_I = "hightemp.txt"
    lists = []
    reverse_list(path_I)