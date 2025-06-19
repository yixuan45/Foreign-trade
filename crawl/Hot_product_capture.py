import os
import requests


class HotProductCrawl:
    def __init__(self, b_name=None, b_url=None):
        """
        初始化函数
        :param b_name: 要爬取的商家名称
        :param b_url: 爬取的商家网址链接
        """
        self.url = ''
        self.b_name = b_name

    def __str__(self):
        return 'This object is used to capture the data of popular products'

    def run(self):
        """
        整个程序的窗口，与main函数的作用相同
        :return:
        """
        pass


if __name__ == '__main__':
    crawler = HotProductCrawl()
    crawler.run()
