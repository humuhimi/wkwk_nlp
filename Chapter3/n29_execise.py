"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

    MediaWiki Action API Code 
    Demo of `Imageinfo`of national flag module: Get information about 
    an image file.
"""

def get_url(tempdict):

    url_re = r"^(http|https)://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$"

    pass


if __name__ == '__main__':
    import requests

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles":"File:Billy_Tipton.jpg",
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA)