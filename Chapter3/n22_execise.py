
"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

→抜けている部分が多い
正規表現を作り直す。
"""

def get_as_word(categorylist):
    words =  []

    for category in categorylist:
        category = category.replace('[[Category:','').replace('|*','').replace(']]','')
        words.append(category)
        # print(category)
    return words

if __name__ == '__main__':

    import n21_execise as n21
    import json
    import re

    path = 'jawiki-country.json'
    # jsonデータ化あらarticle作成
    article = n21.read_json_string(path)
    category_list = n21.get_category_line(article)
    words = get_as_word(category_list)
    for word in words:
        print(word)


# [[Category:]]がいらない


