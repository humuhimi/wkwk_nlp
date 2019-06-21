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
    100    1099   1199   149    249    349    449    50     599    699    799    899    99
    1000   1100   1200   150    250    350    450    500    600    700    800    900    999
    1049   1149   1249   199    299    399    49     549    649    749    849    949
    1050   1150   1250   200    300    400    499    550    650    750    850    950
    1050   1150   1250   200    300    400    499    550    650    750    850    950
    :
    """
    file_path = "words.txt" + input("この中から番号を選んでください\n"+word_index)
    # stemming適応
    stemed = stemming_text(file_path)
    pprint(stemed)





    
