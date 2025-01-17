"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""


text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


def mk_str_array(text):

    lists = text.split(' ')
    mono_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result = {}
    
    # インデックスと値を持ってきて条件にしたがってdict型に代入する。
    for i,l in enumerate(lists):
        if i in mono_list: # 1文字だけのリストにあうか合わないか
            result.update({i:l[:1]})
        else:
            result.update({i:l[:2]})
    else:
        return result


print(mk_str_array(text))