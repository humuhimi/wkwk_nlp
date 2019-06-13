"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

# chr が数字に変換 ord が文字に変換

def cipher(x):
    lists = []
    text = x

    for t in text:
        if t.islower():
            lists.append(str(ord(t)))
        else:
            lists.append(t)
    return ''.join(lists)

if __name__ == '__main__':
    text = "abesAdadA"
    print(cipher(text))





