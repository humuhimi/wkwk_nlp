"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import xml.etree.ElementTree as ET
import re

# ファイルを読み込む
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
prog = re.compile(r'^\n')

output_list = []
tmp_list = []

for child in root.iter():
    if child.tag == 'word':
        word = child.text
    if child.tag == 'lemma':
        lemma = child.text
    if child.tag == 'pos':
        pos = child.text
        
    print('\t'.join([word,lemma,pos]))