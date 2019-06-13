"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""
# this is a pen

import random


def rand_ward_mixer(text):
   
    text = text.split(' ')
    strin = []
    for s in samp:
        # sが4文字以上あるかどうかで並び替えるか放置かを洗濯
        if len(s) > 4:
            # 並び替え
            s = list(s) # リストに入れる
            new_s = random.sample(s[1:-1],k=len(s[1:-1])) # 先頭と末尾以外をランダムサンプリング
            del s[1:-1] # 中間部分を削除してランダムサンプルしたものと代入を使って入れ替える
            s[1:-1] += new_s
        else:
            # 並び替えない
            pass
            # 単語をそれぞれstrinに追加
        strin.append(''.join(s))
# 単語かんにスペースを入れる
    string = ' '.join(strin)
    return string




if __name__ == '__main__':

    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(rand_ward_spliter(text))







