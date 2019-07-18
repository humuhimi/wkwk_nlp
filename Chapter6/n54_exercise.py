"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import xml.etree.ElementTree as ET

# ファイルを読み込む
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()


for sentence in root.findall('document/sentences/'):
    for token in sentence.findall('tokens/'):
        print('単語\tレンマ\t品詞')
        word = token.find('word').text
        lemma = token.find('lemma').text
        POS = token.find('POS').text
        print('\t'.join([word,lemma,POS]))