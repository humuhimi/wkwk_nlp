"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，
各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab
from pprint import pprint

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
       一行ごとの形態素解析結果のマップ型
    result_mapping_list:list
        morphological_dictの全体リスト
    Returns
    --------
    result_mapping_list:mapping dictionary list
    '''
    #先頭に改行があるので削除する
    mecab_file = mecab_file.lstrip('\n')
    # 一行ずつに分割
    raw_list = mecab_file.splitlines()
    result_mapping_list = []

    for temporary_list in raw_list:
        tmp_list = temporary_list.replace('\t',',').split(',')
        # '最終行EOS直前まで読み込む
        if tmp_list[0] == 'EOS':
            break
        else:
            morphological_dict = {'Surface':tmp_list[0],'base':tmp_list[1],'pos':tmp_list[2],'pos1':tmp_list[-3]}
            result_mapping_list.append(morphological_dict)
    
    
    return result_mapping_list

        
mecab_text = text_toMeCab(text_from,text_to)
result = maping_morphology(mecab_text)
pprint(result)

