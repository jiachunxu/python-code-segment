# 批量重命名path路径下所有文件

import os


def batch_rename(path, A):
    # 去掉文件名A字符前面所有字段
    files = os.listdir(path)
    for f in files:
        新文件名 = f[f.index(A):]
        原文件完整路径 = os.path.join(path, f)
        新文件完整路径 = os.path.join(path, 新文件名)
        os.rename(原文件完整路径, 新文件完整路径)

# 测试
# path = r"C:\Users\adminjia\Desktop\雪中悍刀行"
# batch_rename(path, '雪')
