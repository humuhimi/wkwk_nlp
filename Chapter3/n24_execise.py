"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
import re



def get_medias(article):
    

    j = 1

    pattern = r'\[\[File:.*\]\]'
    prog = re.compile(pattern)

    while len(article) > j:

        matches = re.findall(prog,article[j]['text'])
        print('\n------article番号:{0}---------\n'.format(j))
        if matches == []:
            print('メディアなし')
        else:
            for m in matches:
                print(m)
            
        j += 1
    

if __name__ == '__main__':

    import n21_execise as n21
    import json
    import re

    path = 'jawiki-country.json'
    # jsonデータ化あらarticle作成
    article = n21.read_json_string(path)

    get_medias(article)



