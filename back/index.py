import os
from fastapi import FastAPI  # 正确导入方式


class IndexBack(object):
    def __init__(self):
        pass

    def __str__(self):
        return "用于创建后端api的设计"

    def run(self):
        """
        程序的入口
        :return:
        """


if __name__ == '__main__':
    IB = IndexBack()
    IB.run()
