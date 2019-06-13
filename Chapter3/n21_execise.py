"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import json
import re



def read_json_string(path):
    '''
    Parameters
    -----------------
    path: str
        path = 'jawiki-country.json'
    articles2: list
        記事のリスト
    Return
    -----------------
    article
    '''
    article = []

    with open(path,'r') as articles:
        for i,a in enumerate(articles):
                article.append(json.loads(a))

    return article




def get_category_line(article):

    '''
    Parameters
    -----------------
    j: int
        初期値:0
        条件:0<j<206
        article2内のリスト番号として使う
    articles2: list
        jsonファイルの文字列が入ったリスト
    text: str
        article2内のtextを\nで分割した一行ずつのテキストを入れる
    categories
    Return
    -----------------
    categories
    '''
    j = 0
    categories = []

    while len(article) > j:

        text = article[j]['text'].splitlines()

        for line in text:
            # カテゴリーもしくはCategoryがあればその行を出力
            if '[[Category' in line or '[[カテゴリー' in line:
                categories.append(line)
                # print(line)
            else:
                continue
        else:
            j += 1
    return categories

if __name__ == '__main__':

    import json
    import re

    path = 'jawiki-country.json'
    # jsonデータ化あらarticle作成
    article = read_json_string(path)
    # article の カテゴリーがある行を出力する
    get_category_line(article)
 


    








    
