"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json

path = 'jawiki-country.json'


with open(path,'r') as article:
    for a in article:
        article2 = json.loads(a)
        if 'イギリス' in article2['title']:
            print(article2['text'])





