"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""
a = 'パタトクカシーー'

def get_odd_word(string):
    return string[0::2]

print(get_odd_word(a))
