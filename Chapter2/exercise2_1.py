"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
"""
filepath = "hightemp.txt"

with open(filepath, "r") as f:
    line = 0
    for s_line in f:
        line += 1
        print(s_line)

print("行数:{0}".format(line))