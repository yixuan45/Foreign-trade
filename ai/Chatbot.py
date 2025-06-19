import os
import request


class ChatBot(object):
    def __init__(self, api_url=None):
        """

        :param api_url:大模型api接口网址
        """
        self.api_url = api_url

    def __str__(self):
        return "chatbot of web(Customer service robot)"

    def run(self):
        pass


if __name__ == '__main__':
    cb = ChatBot()
    cb.run()
