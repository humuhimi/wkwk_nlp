"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

import MeCab
from pprint import pprint
from n30_execise import maping_morphology
from n31_execise import load_mecab_file,extract_verb_type_all


def extract_pos_pos1_all(analyzed_list,pos="名詞",pos1="サ変接続"):
    '''
    動詞「する」に接続してサ行変格活用の動詞となりうる名詞を抽出する
    pos:str
        今回の場合:名詞
    pos1:str
        今回の場合:サ変接続
    '''
    irreg_conjugate_posList = []
    
    for mapped_morphology in analyzed_list:
        if mapped_morphology['pos'] == pos:
            if mapped_morphology['pos1'] == pos1:
                irreg_conjugate_posList.append(mapped_morphology['base'])
            else:
                continue
        else:
            continue

    return irreg_conjugate_posList


if __name__ == "__main__":

    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)
    # サ変名詞の名詞を全てリスト格納
    nouns_list =  extract_pos_pos1_all(analyzed_list,"名詞","サ変接続")
    pprint(nouns_list)

