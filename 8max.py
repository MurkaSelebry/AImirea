from re import split


def main(s):
    split_list = list(filter(None, split(
        ' |<block>|</block>|let|@|[.]?end|;|=|[.]do|,|\n', s)))
    res = [(split_list[i][1:-1], int(split_list[i + 1])) for i in range(
        0, len(split_list), 2)]
    return res

