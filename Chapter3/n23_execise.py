"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ

== 文化 == :セクション1
=== 音楽 === : セクション2
==== クラシック音楽 ==== : セクション3
===== 高い大学進学率 ===== : セクション4
"""


def get_sect_pt(article,n):
    '''
    Parameters
    -----------------
    text:str
        article
    n:int
        記事の番号
    Return
    -----------------
    None
    '''
    text = article[n]['text']

    pattern = r'={2}.*={2}'
    pattern2 = r'={3}.*={3}'
    pattern3 = r'={4}.*={4}'
    pattern4 = r'={5}.*={5}'
    sect = re.compile(pattern)
    sect2 = re.compile(pattern2)
    sect3 = re.compile(pattern3)
    sect4 = re.compile(pattern4)

    section = set(re.findall(sect,text))
    section2 = set(re.findall(sect2,text))
    section3 = set(re.findall(sect3,text))
    section4 = set(re.findall(sect4,text))

    section3 = section3 - section4
    section2 = section2 - section3 - section4
    section = section - section2 - section3 - section4


    print("セクション1:{0}\n\nセクション2:{1}\n\nセクション3:{2}\n\nセクション4:{3}\n\n".format(section,section2,section3,section4))

    # return section,section2,section3,section4
    

if __name__ == '__main__':

    import json
    import re
    import n21_execise as n21

    path = 'jawiki-country.json'
    # jsonデータ化あらarticle作成
    article = n21.read_json_string(path)
    n = int(input("記事番号を入力してください:"))
    get_sect_pt(article,n)


