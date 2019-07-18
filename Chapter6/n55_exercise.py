"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import xml.etree.ElementTree as ET

# ファイルを読み込む
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()



for sentence in root.findall('document/sentences/'):
    for token in sentence.findall('tokens/'):
        word = token.find('word').text
        if "PERSON" == token.find('NER').text:
            print(word)
