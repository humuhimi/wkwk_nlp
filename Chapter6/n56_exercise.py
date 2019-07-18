"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
representative mention (mention)
"""

import xml.etree.ElementTree as ET

# ファイルを読み込む
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for coreference in root.findall('document/coreference/'):
    for mention in coreference.findall('mention'):
        print(mention.tag)
        print(mention.attrib.values())
        for mention_value in mention.attrib.values():
            if mention_value == 'true':
                mention.tag = "representative mention (mention)"
                print(mention.tag)

tree.write('retag.xml')
print('ファイルの書き込み終了')
