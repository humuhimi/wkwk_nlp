"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
import itertools

# bi-gramを作る
def make_str_bigram(text,n=2):

    text = list(text)
    iterr = itertools.combinations(text,n)
    lists = []
    for i in iterr:
        lists.append(i)
    return lists


def ck_groups(X,Y): # 集合をチェックする
    union = X.union(Y) # 和集合
    diff = X.difference(Y) # 差集合
    product = X.intersection(Y) # 積集合
    print("和集合:{0}\n差集合:{1}\n積集合:{2}\n".format(union,diff,product))

    return union,diff,product


def find_se(X,Y):

    if 'se' in X or 'se' in Y:
        if 'se' in X:
            print('seはXに含まれる')
        else:
            print('seはYに含まれる')
    else:
        print('seは含まれない。')



text1 = "paraparaparadise"
text2 = "paragraph"

input_X = set(make_str_bigram(text1,2))
input_Y = set(make_str_bigram(text2,2))

ck_groups(input_X,input_Y)

find_se(input_X,input_Y)
