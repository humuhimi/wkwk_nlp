"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，
=====
各形態素は表層形（surface），
基本形（base），
品詞（pos），
品詞細分類1（pos1）
====
をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．

表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

表層形,品詞,品詞細分類1

当たる、ない:基本形
"""

import MeCab

#ファイルのパス用
text_from = "neko.txt"
text_to = "neko.txt.mecab"

def text_toMeCab(text_from,text_to):
    '''
    convert mecab morphological analisis result and  write it to text

    Parameters
    --------------

    mecab_tag: メカブオブジェクト
    origin: 元のファイル先
    as_mecab: メカブに変更するファイル先

    Returns
    --------
    parsed_text
    '''
    # メカブタグ
    mecab_tag = MeCab.Tagger('')

    with open(text_from,'r') as origin,\
         open(text_to,'w') as as_mecab:
        tmp_text = origin.read()
        parsed_text = mecab_tag.parse(tmp_text)
        as_mecab.write(parsed_text)

        return parsed_text
    


def maping_morphology(mecab_file):
    '''
    mapping morphological analysis result
    
    Parameters
    ----------
    all_text:str
        「吾輩は猫である」全文読み込み
    raw_list:list
        改行ごとにsplit されたもの(要素)
    temporary_list,tmp_list:list
        一時変換用リスト
    morphological_dict:dict
       形態素解析結果のマップ 
    Returns
    --------
    morphological_dict:mapping dictionary
    '''
    raw_list = mecab_file.split('\n')
    morphological_dict = {}

    for temporary_list in raw_list:
        tmp_list = temporary_list.split('\t')
        morphological_dict.update({'surface':tmp_list[0],
                                    'base':tmp_list[2],
                                    'pos':tmp_list[3],
                                    'pos1':tmp_list[-3]})
    return morphological_dict

        
mecab_text = text_toMeCab(text_from,text_to)
result = maping_morphology(mecab_text)
print(result)

