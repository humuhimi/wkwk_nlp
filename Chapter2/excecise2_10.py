"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
from collections import Counter





def get_high_frequency(path):

    path_i = path
    pref = []
    lists = []

    with open(path_i,'r') as I:
        for i in I:
            lists.append(i.split('\t'))

    

    for l in lists:
        pref.append(l[0])

    pref_counter = Counter(pref)
    pref_dict = dict(pref_counter.most_common())

    for i in lists:
         if i[0] in pref_dict.keys():
             i.insert(0,pref_dict[i[0]])

    lists = sorted(lists,reverse=True)

    for i in lists:
        i.pop(0)
        print('\t'.join(i))

    



if __name__ == '__main__':
    

    path_I = "hightemp.txt"
    lists = []

    get_high_frequency(path_I)


   


