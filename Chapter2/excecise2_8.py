"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""
path = 'hightemp.txt'
row = []

with open(path,'r') as f:
    for line in f:
        row.append(line.split('\t'))



row[0][0]

sets = []

for  i in range(len(row)):
    sets.append(row[i][0])

sets = set(sets)

print(sets,len(sets))



