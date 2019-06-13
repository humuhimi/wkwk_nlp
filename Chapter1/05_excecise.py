"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
""" 
import itertools


text = "I am an NLPer"


def make_str_bigram(text,n=2):

    # 単語をリスト化する
    # リスト内のspaceをlambdaを使って取り除く
    # textに入れなおす

    text = list(filter(lambda s:s != ' ',list(text)))
    iterr = itertools.combinations(text,n) # テキストと組み合わせの文字数でイテレータ型を作りループし出力する
    for i in iterr:
        print(i)


def make_word_bigram(text,n=2):

    text = text.split(' ')
    iterr = itertools.combinations(text,n)
    for i in iterr:
        print(i)



make_str_bigram(text)
make_word_bigram(text)



