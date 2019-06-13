def chg_temp_content_todict(temp_list:list):

    key_list = []
    value_list = []

    for i in temp_list:
        splited = line.split('=')     
        keys_list.append(splited[0])
        values_list.append(splited[1])
    
    temp_dict = dict(zip(key_list,value_list))
    return temp_dict



def remove_markup(pattern,text):
    
        # 辞書型の場合

    if type(text) != 'list':
        renew = {}
        text = list(text.items())

        for k,v in text: 
            k = re.sub(pattern,"",k)
            v = re.sub(pattern,"",v)
            dictionary = {k:v}
            renew.update(dictionary)
        return renew
    else:
        # str型の場合
        renew = []

        for t in text:       
            t = re.sub(pattern,"",t)
            renew.append(t)
        
        return renew





def remove_all_markup(text):
    # ''などのマークアップを削除する
    pattern26 =  r"\'\'\'(?!')|\'\'(?!')|\'(?!')"

    new26 = remove_markup(pattern26,text)
    print(new26[1])

    # [[|]]のパターン
    pattern27_2 = r"|\[\[.{10}\|(?!\[){2}.{10}\]\]|\[{2}|\]{2}"
    # |のパターン
    pattern27_3 = "|\|" 
    pattern =   pattern27_2 +pattern27_3
    
    new27 = remove_markup(pattern,new26)

    # {{ }}はけす

    pattern28_1 = r"\{\{\s?|\s?\}\}"
    pattern28_2 = "|</?{[a-z]{2,12}\?/?>?|redirect"
    # pattern28_3 = "|<references />|redirect"


    pattern = pattern28_1+pattern28_2

    new28 = remove_markup(pattern,new27)


    return new28


    





        

            
            








