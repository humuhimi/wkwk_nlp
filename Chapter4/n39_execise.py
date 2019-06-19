"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import MeCab
from pprint import pprint
import collections
from n30_execise import maping_morphology
from n31_execise import load_mecab_file
from n36_execise import extract_type_all,extract_frequent_words
from n37_execise import create_words_frequency_graph
import matplotlib.pyplot as plt
import pandas as pd


#  TODO:freq_count　出現頻度の順序化
def freq_to_order(freq_count):

    freq_count = list(freq_count)
    uniq_freq = list(set(freq_count))
    uniq_freq.sort(reverse=True)

    freq_order_list = []

    for index,_uniq in enumerate(uniq_freq):
        for _frequency in freq_count:
            if _uniq == _frequency:
                freq_order_list.append(int(index+1))
            else:
                continue
    
    return freq_order_list


# TODO:順序と出現頻度共に対数化する

# TODO:グラフ作成 その他弊害



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
    print(freq_count)
    # グラフ作成
    # create_words_frequency_graph(freq_value,freq_count,graph='hist',title="出現頻度の高い単語のヒストグラム",xlabel="出現頻度",ylabel="出現頻度をとる単語の種類数")
    # HACK:イメージとしてデータがある場所の上に値が表示されるようにしたい。


    
