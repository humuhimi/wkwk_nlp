import MeCab
from pprint import pprint
import collections
from n30_execise import maping_morphology
from n31_execise import load_mecab_file
from n36_execise import extract_type_all,extract_frequent_words
import matplotlib.pyplot as plt
import pandas as pd

# グラフの種類、出現単語、出現回数

def create_words_frequency_graph(x,y,graph='bar',title="",xlabel="",ylabel="",y_lim=[0,10000],_grid=None,log_log=False):
    '''
    とりあえず、bar　plot で出力する
    日本語フォント
    FIXME:histogramの時だけbins=bins_が必要?分岐する必要あり(default bins_=False)

    '''
    igfont = {'family':'IPAexGothic'}
    plt.rc('font',**igfont)

    data = pd.Series(y,index=x)
    data.plot(kind=graph,label=y,grid=_grid,loglog=log_log)
    plt.title(title,**igfont)
    plt.xlabel(xlabel,**igfont)
    plt.ylabel(ylabel,**igfont)
    plt.ylim(y_lim)

    plt.show()


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
    freq_value,freq_count = extract_frequent_words(surface_list,N=10)
    print(freq_value,freq_count)
    # グラフ作成
    create_words_frequency_graph(freq_value,freq_count,title="出現頻度の高い単語グラフ",xlabel="出現単語",ylabel="出現頻度",y_lim=[0,9000])

