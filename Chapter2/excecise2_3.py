"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ
"""

#  一列目をcol1.txtに，2列目をcol2.txtに変換する

path_r = "hightemp.txt"
path_w1 = "col1.txt"
path_w2 = "col2.txt"


lines = ''
# with open(path_r,'r') as f:
    # with open(path_w1,'w') as w1:
    #     with open(path_w2,'w') as w2:
with open(path_r,'r') as f,\
     open(path_w1,mode='w') as w1,\
     open(path_w2,mode='w') as w2:
            for line in f:
                # 高知県  江川崎  41      2013-08-12
                line = line.split('\t')
                w1.write(str(line[0]+'\n'))
                w2.write(str(line[1]+'\n'))

          
        
