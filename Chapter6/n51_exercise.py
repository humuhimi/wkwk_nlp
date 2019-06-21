"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""
from nltk import sent_tokenize
from pprint import pprint
from n50_exercise import load_text,find_specialchar_index,sent_tokenize_Plus
import re


# split by 空白
def sentence_ToWords(tokens):
    '''
    文章を単語にする

    Parameter
    ========
    words_list:list
        センテンスの単語全て
    sentence:
        文章トークン化されたもの
    Return
    ========    
    words_list,len(words_list)
    '''
    words_list = []
    word_spliter = re.compile(r"\s")

    for token in tokens:
        words_list.extend(word_spliter.split(token))
    
    return words_list,len(words_list)

# 50個ずつまとめる+最後に空行 |別ファイルに書きこむ

def write_50word_ToText(word_list,word_len):
    '''
    新規ファイルに50文字づつ単語を書きこむ。
    PArameter
    ========
    PATH:str
        ファイルのパス
    path:str
        新規生成されるファイルのパス(末尾には何個目までのファイルが入ってるかが入る)
    start:int
    end:int
        50区切りのために使用(単語のインデックス)
    re_format:
         単語以外の文字列を削除するためのもの
    '''
    PATH = "words.txt"
    start = 0
    end = 49

    re_format = re.compile(r"""
    \(| # (
    \)| # )
    \.| # .
    , |# ,
    \"| # "
    \\n{2} # 空白2連続
    """,re.VERBOSE)

    while word_len > end:
        path = PATH + str(end)
        with open(path,'w') as file:
            for word in word_list[start:end]:
                # maxで4回単語フォーマット化処理すると仮定
                word = re_format.sub('',word,4)
                file.write(word+'\n')
            else:
                file.write('\n')
                start = end
                end += 50
                      

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
    samp_text,length = sentence_ToWords(sent_token)
    # samp を区切る

    write_50word_ToText(samp_text,length)


    
