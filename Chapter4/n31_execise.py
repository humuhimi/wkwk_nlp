"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""
import MeCab
from pprint import pprint
from n30_execise import maping_morphology



def load_mecab_file(mecab_file):
    '''
    mecabファイルを読み込む
    '''
    with open(mecab_file) as mecab_data:
        mecab_text = mecab_data.read()
    
    return mecab_text


def extract_verb_type_all(analyzed_list,type="Surface"):
    '''
    動詞の表層形をすべて抽出する
    '''
    verb_surface_list = []

    for mapped_orphology in analyzed_list:
        if mapped_orphology['pos'] == '動詞':
            verb_surface_list.append(mapped_orphology[type])
    
    return verb_surface_list


if __name__ == '__main__':

    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)
    # 動詞の表層を全てリスト格納
    verb_list = extract_verb_surface_all(analyzed_list)  

    pprint(verb_list)