"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import MeCab
from pprint import pprint
from n30_execise import maping_morphology
from n31_execise import load_mecab_file,extract_verb_type_all



def extract_noun_continuos(analyzed_list):
    '''
    最長一致で名詞を連接したリストを出力する
    HACK:動詞の連結や助詞の連結なども作成できる?
    '''
    noun_join_list = []
    join_box = ""

    for mapped_morphology in analyzed_list:
        if mapped_morphology['pos'] == "名詞":
            join_box += mapped_morphology['Surface']
        elif join_box == "":
            continue
        else:
            noun_join_list.append(join_box)
            join_box = ""
            continue

    return noun_join_list


if __name__ == "__main__":
    
    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)
    # 連続する名刺をリスト格納
    noun_join_list = extract_noun_continuos(analyzed_list)
    print( noun_join_list)
