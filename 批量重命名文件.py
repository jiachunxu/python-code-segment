# 批量重命名path路径下所有文件

import os


def 去掉文件名A字符前的全部字符(path, A):
    """

    :param path: 文件路径
    :param A: 文件名第一个有用字符
    """
    files = os.listdir(path)
    for f in files:
        新文件名 = f[f.index(A):]
        原文件完整路径 = os.path.join(path, f)
        新文件完整路径 = os.path.join(path, 新文件名)
        os.rename(原文件完整路径, 新文件完整路径)
