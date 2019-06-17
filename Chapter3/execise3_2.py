"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""


import json
import re


path = 'jawiki-country.json'

json_lists = []
json_dict = {}
category_list = []


def mk_category_pt():
    """
    英語　日本語　カテゴリー文字列を検索するための正規表現のパターンを作る関数
    パターンを正規表現で作りコンパイルしている

    Parameters
    -------------
    pattern1,2: str
        正規表現の文字列
    prog1,2: re.Pattern
        コンパイルされた正規表現のパターン
    
    Return
    --------------
    prog,prog2

    """
    
    pattern = r'\[\[カテゴリ\:.+\]\]'
    pattern2 = r'\[\[Category\:.+\]\]'
    prog = re.compile(pattern)
    prog2 = re.compile(pattern2)

    return prog,prog2


prog,prog2 = mk_category_pt()

with open(path,'r') as article:
    for a in article:
             article2 = json.loads(a)
             category = re.findall(prog,article2['text'])
             category2 = re.findall(prog2,article2['text'])
             category.extend( category2)
             category_list.append(category)

print(category_list)

# print(article2['title'])

# print(json_lists[0])
# print(json_dict)

# for i in json_lists[0]:
#     # if 'カテゴリ' in i:
#     print("<br><br><br>")
#     print(i)

        # if 'カテゴリ' in a_json['text']:
        #     print('title!!:{0}'.format(a_json['title']))
        #     print(a_json['text'])
        #     break;
