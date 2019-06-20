"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
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
    # グラフ作成
    # FIXME:hist グラムが雑すぎる　とりあえずこれで一回通す
    create_words_frequency_graph(freq_value,freq_count,graph='hist',title="出現頻度の高い単語のヒストグラム",xlabel="出現頻度",ylabel="出現頻度をとる単語の種類数",y_lim=[0,9000])
    # HACK:イメージとしてデータがある場所の上に値が表示されるようにしたい。
