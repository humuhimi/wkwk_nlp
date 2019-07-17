"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import pprint
import re
from nltk import sent_tokenize
from nltk.stem import PorterStemmer
from pprint import pprint
from n50_exercise import load_text,find_specialchar_index,sent_tokenize_Plus
from n51_exercise import sentence_ToWords,write_50word_ToText
import nltk.parse.corenlp
from nltk.parse import CoreNLPParser
import corenlp


path = "nlp.txt"


# print(a)


if __name__ == "__main__":
    
    path = "nlp.txt"
    # テキストの読み込み
    sentence = load_text(path)
    # 特殊な文字の位置を取得する
    index = find_specialchar_index(sentence)
    # token化　一文化
    sent_token = sent_tokenize_Plus(sentence,index)
    print(sent_token[0])
    parser = CoreNLPParser(url='http://localhost:9000')
    

a = list(parser.parse(sent_token))

   
