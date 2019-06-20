"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""


def print_arg(x, y, z):
    """
    3つの引数をもとに一つの文字列を返す

    Parameters:
    ---------------
    x: int
    y: str
    z: float
    """
    print("{0}時の{1}は{2}".format(x, y, z))
    # return "{0}時の{1}は{2}".format(x,y,z)もできる


if __name__ == "__main__":
    x = 12
    y = "気温"
    z = 22.4
    print_arg(x, y, z)
