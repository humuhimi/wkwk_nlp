def extract_noun_type_all(analyzed_list,type="Surface"):
    '''
    名詞の表層形をすべて抽出する
    '''
    noun_type_list = []

    for mapped_morphology in analyzed_list:
        if mapped_morphology['pos'] == '名詞':
            noun_type_list.append(mapped_morphology[type])
    
    return noun_type_list

    
def extract_pos_type_all(analyzed_list,pos="動詞",type="Surface"):
    '''
    品詞(名詞、動詞など選択できる)の形(表層系、品詞、基本形など選択可能)をすべて抽出する
    * 後付で作ったので名前から関数の概要がわかりにくすぎる:FIXME:HACK
    '''
    pos_type_list = []

    for mapped_morphology in analyzed_list:
        if mapped_morphology['pos'] == pos:
            pos_type_list.append(mapped_morphology[type])
    
    return pos_type_list