
"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""
from nltk import sent_tokenize
from pprint import pprint

def load_text(path):
    '''
    テキストの読み取り
    '''
    
    with open(path,'r') as data:
        sentence = data.read()
    
    return sentence

def find_specialchar_index(sentence,character=":"):
    '''
    １度だけindex返す
    FIXME:indexのリストを返すべき
    '''
    for index,sent in enumerate(sentence):
        if sent == character:
            return int(index+1)

def sent_tokenize_Plus(sentence,index):
    '''
    特定文字がある場所に#を代入する。
    # を基準に分割する
    それぞれのリストをtoken化する
    tokenを結合する。
    '''
    sentence = sentence[:index] +  '#' + sentence[index:]
    sent_splited = sentence.split('#')

    sent_token = []
    for i in range(len(sent_splited)):
        token = sent_tokenize(sent_splited[i])
        sent_token.extend(token)
    
    return sent_token



if __name__ == "__main__":

    from nltk import sent_tokenize
    from pprint import pprint
    import re

    path = "nlp.txt"

    # テキストの読み込み
    sentence = load_text(path)
    # 特殊な文字の位置を取得する
    index = find_specialchar_index(sentence)
    # token化　一文化
    sent_token = sent_tokenize_Plus(sentence,index)
    
    pprint(sent_token)
