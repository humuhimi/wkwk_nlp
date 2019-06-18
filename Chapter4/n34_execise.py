"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．

板の間	名詞,一般,*,*,*,*,板の間,イタノマ,イタノマ
木の根	名詞,固有名詞,地域,一般,*,*,木の根,キノネ,キノネ
日の出	名詞,一般,*,*,*,*,日の出,ヒノデ,ヒノデ
"""

import MeCab
from pprint import pprint
from n30_execise import maping_morphology
from n31_execise import load_mecab_file

def define_exception_ofX():
    '''
    extract_concat_noun_withXで使う例外文字列を記述する

    Parameters
    ==========
    e_string:list
        除外1(文字列)「この」と「その」以外
    e_max_len;int
        除外2(文字数) 6文字以上
    Returns
    =======
    e_string,e_max_len
    '''
    e_string = ['この','その']
    e_max_len = int(6)

    return e_string,e_max_len




def extract_concat_noun_withX(analyzed_list,x='の',Exceptions=define_exception_ofX()):
    '''
    特定の文字で名詞を二つ以上の名詞に分離する

    X:str
        分離用の文字:今回はの
    '''

    concat_noun_list = []

    e_string,e_max_len = Exceptions

    for mapped_morphology in analyzed_list:
        if mapped_morphology['pos'] == '名詞':
            # 先頭末尾以外に'の'がある場合
            if x in  mapped_morphology['Surface'][1:-1]:
                # FIXME  e_string[0]  e_string[1]を綺麗に持ってくる方法を知りたい。
                # 「その」、「あの」が入ってる場合はcontinue 
                if  e_string[0] in mapped_morphology['Surface'] or e_string[1] in mapped_morphology['Surface']:
                    continue
                elif len(mapped_morphology['Surface']) > e_max_len:
                    continue
                else:
                    concat_noun_list.append(mapped_morphology['Surface'])

    return concat_noun_list


if __name__ == "__main__":
    
    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)

    # 2つの名詞が「の」で連結されている名詞句を抽出
    concat_nouns = extract_concat_noun_withX(analyzed_list)

    print(concat_nouns)