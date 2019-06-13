"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""
# アルファベットのリストを作る。
# 大文字、小文字に注意する。
# ヒットした順番から別のリストの中に入れる。


text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# upper-case A-Z
ALP = [chr(i) for i in range(65,65+26)]
# lower-case a-z
alp = [chr(i) for i in range(97,97+26)]
lists = []
for t in text:
    if t in alp or t in ALP:
        lists.append(t.lower())

print('順番:')
print(''.join(lists))



