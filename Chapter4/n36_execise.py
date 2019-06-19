"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import MeCab
from pprint import pprint
import collections
from n30_execise import maping_morphology
from n31_execise import load_mecab_file

# TODO:surfaceのリストだけを取り出す→何か関数

def extract_type_all(analyzed_list,type="Surface"):
    '''
    type(表層系、品詞、基本形など選択可能)をすべて抽出する
    default SUrface
    '''
    type_list = []

    for mapped_morphology in analyzed_list:
            type_list.append(mapped_morphology[type])
    
    return type_list

#TODO:Counter.most_common(取り出す要素数(N個):None)[要素番号][Surface] 高い順　低い順

def extract_frequent_words(words_list,reverse=0,N=None):
    '''
    words_lists:単語の群
    reverse：逆順に取り出すか
    N:取り出す個数
    '''
    if reverse == 1:
        freq_counter = collections.Counter(words_list).most_common(N)[::-1]
    else:
        freq_counter = collections.Counter(words_list).most_common(N)

    freq_value,freq_count = zip(*freq_counter)

    return freq_value,freq_count



if __name__ == "__main__":
    
    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)
    # 表層形だけを取り出したリストを作成する
    surface_list = extract_type_all(analyzed_list)
    # 出現頻度の高い値とその回数を取り出す
    freq_value,freq_count = extract_frequent_words(surface_list)

    print(freq_value)
