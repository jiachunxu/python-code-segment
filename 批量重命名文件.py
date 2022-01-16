# 批量重命名path路径下所有文件

import os


def batch_rename(path, A):
    # 去掉A字符前面所有字段
    files = os.listdir(path)
    for f in files:
        str = f[f.index(A):]
        原来的文件路径 = os.path.join(path, f)
        新的文件名 = os.path.join(path, str)
        os.rename(原来的文件路径, 新的文件名)

# 测试
# path = r"C:\Users\adminjia\Desktop\雪中悍刀行"
# batch_rename(path, '雪')
