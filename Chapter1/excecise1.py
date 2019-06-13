a = 'stressed'
# 文字を配列に取り込み　逆にだす。
norm = []
rev = []
i = 1
strlen = len(a)

while strlen >= i:

    rev.append(a[-i])
    i += 1
reversed = ''.join(rev)
print(reversed)


     


