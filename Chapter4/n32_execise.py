import MeCab
from pprint import pprint
from n30_execise import maping_morphology
from n31_execise import load_mecab_file,extract_verb_type_all




if __name__ == '__main__':
    
    # ファイルパス
    mecab_file = "neko.txt.mecab"

    # neko.txt.mecabを読み込む
    mecab_text = load_mecab_file(mecab_file)

    # 形態解析後のマッピングリスト
    analyzed_list = maping_morphology(mecab_text)
    # 動詞の原型を全てリスト格納
    verb_list = extract_verb_type_all(analyzed_list,"base") 
    pprint(verb_list)

