"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

stanford-corenlp-full-2018-10-05.zipをダウンロード
cd stanford-corenlp-full-2018-10-05
./corenlp.sh -file nlp.txt
mv nlp.txt.xml Chapter6/
"""


import pprint
import xml.etree.ElementTree as ET
import re

# ファイルを読み込む
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
prog = re.compile('^\n')


for word in root.itertext():
        if not re.match(prog,word):
            print(word)



