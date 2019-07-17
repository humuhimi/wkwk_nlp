"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""
import re
from nltk import sent_tokenize
from nltk.stem import PorterStemmer
from pprint import pprint
from n50_exercise import load_text,find_specialchar_index,sent_tokenize_Plus
from n51_exercise import sentence_ToWords,write_50word_ToText



def stemming_text(file_path):
    '''
    stem word in text file
    '''
    stemed = []
    ps = PorterStemmer()

    with open(file_path,'r') as file:
        line = file.readline()
        while line:
            stem = ps.stem(line.rstrip())
            stemed.append(stem+'    '+line[len(stem):].rstrip())
            line = file.readline()
    return stemed


if __name__ == "__main__":
    
    path = "nlp.txt"
    # テキストの読み込み
    sentence = load_text(path)
    # 特殊な文字の位置を取得する
    index = find_specialchar_index(sentence)
    # token化　一文化
    sent_token = sent_tokenize_Plus(sentence,index)
    # print(sent_token[0])
    # とりあえず一区切りだけ入れる
    words,length = sentence_ToWords(sent_token)
    # 単語書き込み
    write_50word_ToText(words,length)
    # ファイルを指定
    word_index = """
1049   149    399    599    849
1099   199    449    649    899
1149   249    49     699    949
1199   299    499    749    99
1249   349    549    799    999
    :
    """
    file_path = "words.txt" + input("この中から番号を選んでください\n"+word_index)
    # stemming適応
    stemed = stemming_text(file_path)
    pprint(stemed)





    
