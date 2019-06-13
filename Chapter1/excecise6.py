"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""
# n-gram n個の文字で分割する。
# 文字列やリストからn-gramを作る。
# 例えば，「図書館情報学」をバイグラムで分割すると，「図書」「書館」「館情」「情報」「報学」となる
# 連続したn文字の候補を取ってくる。
# I amから2文字なら、Ia[0,1] とam[1,2] len(2)
# 0,1 1,2 2,3 3,4 (n=2,)

def mk_ngram_list(text,n): # text: 文章,n:何文字区切りか
    text = text
    samp = list(''.join(text.split()))
    
    lists =  []
    m = 1-n

    for i in range(0,len(samp)+m):
        sample = ''
        for k in range(n):
            sample += samp[i+k]
            # lists.append(samp[i]+samp[i+1]+samp[i+2]+samp[i+3]) # 3個入れる
        lists.append(sample)
    
    return lists



if __name__ == '__main__':



    text = "I am an NLPer"
    samp = list(''.join(text.split())) # ['I', 'a', 'm', 'a', 'n', 'N', 'L', 'P', 'e', 'r']
    # print(list(samp))

    #----------1
    lists =  []

    for i in range(0,len(samp)-1):
        print(i)
        lists.append(samp[i]+samp[i+1]) # 2個入れる

    print(lists)

    #-----------2 
    lists =  []
    for i in range(0,len(samp)-2):
        print(i)
        lists.append(samp[i]+samp[i+1]+samp[i+2]) # 3個入れる

    print(lists)
    #---------3 
    lists =  []
    for i in range(0,len(samp)-3):
        print(i)
        lists.append(samp[i]+samp[i+1]+samp[i+2]+samp[i+3]) # 3個入れる

    print(lists)

    #---------- def

    mk_ngram_list()
    print(mk_ngram_list(text,6))








    # n+m = 1
    # n = 2 ->m = -1
    # n = 3 ->m =  -2
    # n = 4 → m = -3 






