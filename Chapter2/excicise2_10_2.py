"""
他の人のコード

"""
from itertools import groupby

fname = 'hightemp.txt'

# 都道府県名の読み込み
lines = open(fname).readlines()
kens = [line.split('\t')[0] for line in lines]

kens.sort()
result = [(ken,len(list(group))) for ken,group in groupby(kens)]

# 出現頻度でソート

result.sort(key=lambda ken:ken[1],reverse=True)
for ken in result:
    print('{ken}({count})'.format(ken=ken[0], count=ken[1]))


