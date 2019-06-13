
"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

a = 'stressed'

# スライスを使って逆転させる

def reverse_str(text): # 名前をわかりやすくする
    return text[::-1] 


print(reverse_str(a))