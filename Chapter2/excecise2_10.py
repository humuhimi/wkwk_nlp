"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
from collections import Counter


def strlist_from_file(path):
    """
    テキストファイルを読み込みstrのlistを返す
    :param path: テキストファイルのパス
    :return: strのリスト
    """
    with open(path, "r") as f:
        lines = f.readlines()
        lines_col1 = [lines[i].split("\t")[0] for i in range(len(lines))]
        return lines_col1


def to_freq_dict(target_list):
    """
    与えられたlistから出現頻度のdictを作成する
    :param target_list: 文字列のlist
    :return: {str: freq(int)}のdict
    """
    return dict(Counter(target_list))


# TODO: ファイル読み込みと出現頻度確認の関数を分ける
def get_high_frequency(path):

    path_i = path
    pref = []
    lists = []

    # リスト作成するならなるべくリスト内包表記使いたい
    with open(path_i, "r") as I:
        for i in I:
            lists.append(i.split("\t"))

    for l in lists:
        pref.append(l[0])

    pref_counter = Counter(pref)
    pref_dict = dict(pref_counter.most_common())

    # ここまで色々やらなくてもdictをsortedすれば無問題
    # 参考リンク: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    for i in lists:
        if i[0] in pref_dict.keys():
            i.insert(0, pref_dict[i[0]])

    lists = sorted(lists, reverse=True)

    for i in lists:
        i.pop(0)
        print("\t".join(i))


if __name__ == "__main__":

    path_I = "hightemp.txt"
    lists = []

    get_high_frequency(path_I)

    result = strlist_from_file(path_I)
    freq_dict = to_freq_dict(result)

    # 結果の表示。ここはもう少しやりようがありそう
    print(freq_dict)
    print(sorted(freq_dict, key=freq_dict.get, reverse=True))
