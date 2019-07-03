"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

<解答例の実行例>
python excecise2_5.py -input_n 10
"""
import argparse

FILEPATH = "hightemp.txt"


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-input_n", required=False, type=int, default=2
    )  # 引数が整数で入るとは限らないのでなんらかのバリデーションが必要
    return parser.parse_args()


if __name__ == "__main__":
    print("start")
    args = arg_parser()
    target_N = args.input_n

    with open(FILEPATH, "r") as f:
        lines = f.readlines()
        print("".join(lines))

        print("\nShow result:\n-----------")
        for i, line in enumerate(lines):
            if i < target_N:
                print(str(i + 1), line, end="")
