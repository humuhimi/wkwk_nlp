"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

1.分割するファイル数を入力
2.分割ファイル数より分割行数を計算する
3.リストから分割行分別ファイルに書き込み　書き込んだ分はリストから削除する
3.5リストのループを終わらせる。
4.最後分割数以下のファイルを全て書き出す。(残ったリストを全て書き出す)
"""

def make_list(path):
        path_i = path
        with open(path_i,'r') as I:
            for i in I:
                lists.append(i)
        return lists;

# ファイル数と分割行数を決める
def decide_size():
    N = int(input('分割ファイル数を入力してください:'))
    



    




    # N1 = int(input('分割ファイル数を入力してください:'))

    # N2 = 

if __name__ == '__main__':

    import string
    a_Z = string.ascii_letters

    path_I = "hightemp.txt"
    path_O = "path_f_splited.txt"

    lists = []

    lists = make_list(path_I)
    print(lists)
