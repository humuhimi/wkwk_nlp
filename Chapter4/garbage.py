# ストップワードの除去：使用頻度の高い言葉を処理対象外にする
import MeCab
# mecab-ipadic-NEologd辞書指定してオブジェクト生成
tagger = MeCab.Tagger()
tagger.parse("")
# 形態素解析の結果をリストで取得、単語ごとにリストの要素に入ってる
node = tagger.parseToNode("機械学習をマスターしたい。")
result = []
 
#助詞や助動詞は拾わない
while node is not None:
    # 品詞情報取得
    # Node.featureのフォーマット：品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞"]:
        # 表層形の取得、単語の文字が入ってる
        result.append(node.surface)
    elif hinshi in["動詞","形容詞"]:
        # 形態素情報から原形情報取得
        result.append(node.feature.split(",")[6])
    node = node.next
 
print(result)
