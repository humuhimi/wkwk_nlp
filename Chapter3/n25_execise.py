

def get_one_text(article,article_number):
    '''
    get article from article num
    '''

    n = article_number

    text = article[n]['text']
    text = text.splitlines()
    
    return text

def mk25regex_checker():
    '''
    templateを探す正規表現
    start:{{ 基礎情報 }}
    end:}}, or }}
    '''
    
    break_pt = r'}},?'
    break_point = re.compile(break_pt)

    return break_point

def mk25template(temp_name):
    '''
    文字列からテンプレート作成
    template: {{ ' 基礎情報 ' }}
    '''
    template = '{{  ' + temp_name + ' }}'

    return template

def get_temp_content(text,template,breakpoint)->list:

    '''
    flag =0
        :continue
    flag =1
        :append in list
    '''

    temp_list = []

    flag = 0

    for i,line in enumerate(text):

        if '{{ 基礎情報 }}' in line:
            print('aaa')
            flag = 1
            continue
        elif re.match(breakpoint,line):
            flag = 0
            break
        elif flag == 1:
            temp_list.append(line)

    return temp_list

def chg_temp_content_todict(temp_list:list):
    
    key_list = []
    value_list = []

    for i in temp_list:
        splited = i.split('=') 
        # splited = splited[0].strip()
        key_list.append(splited[0])
        value_list.append(splited[1])
    
    temp_dict = dict(zip(key_list,value_list))
    # for key,value in dicts.items():
    #     print("{0}:{1}".format(key,value))
    return temp_dict


if __name__ == '__main__':

    """
    プログラム内容
    ------------
    25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
    """

    # n21_execise.pyのモジュールをインポート

    import n21_execise as n21_task 
    import json
    import re

    n = int(input("記事番号を入力してください"))

    # wikipageのjsonファイルパス
    path = 'jawiki-country.json'

    # jsonデータでlist型変数:article作成
    article = n21_task.read_json_string(path)

    text = get_one_text(article,n)

    breakpoint = mk25regex_checker()
    template = mk25template("基礎情報")

    temp_list = []

    temp_list = get_temp_content(text,template,breakpoint)

    dicts = []

    dicts = chg_temp_content_todict(temp_list)
    print(dicts)
    # print(temp_list)
    # print(template)
    # print(breakpoint)


    for key,value in dicts.items():
        print("{0}:{1}".format(key,value))


    '''
    おそらくtext 1以外では基礎情報が出る場所が違う故に変なバグが起こる。
    →つまり2行目からとか変な文字が入ってると読み取れないとかあるんやと思う。

    記事番号を入力してください3
aaa
Traceback (most recent call last):
  File "n25_execise.py", line 108, in <module>
    dicts = chg_temp_content_todict(temp_list)
  File "n25_execise.py", line 72, in chg_temp_content_todict
    value_list.append(splited[1])
IndexError: list index out of range

# splited = splited[0].strip()→これがデータを持って来れないとか変な分割をする原因や
→この機能要件を他で満たす

また、index10以降が動かない。→原因
    '''


  

    


