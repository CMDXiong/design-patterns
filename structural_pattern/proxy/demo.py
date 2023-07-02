# -*- coding:utf-8 -*-
__author__ = 'px'

"""
代理类在程序运行时创建的代理方式被成为动态代理

可见，通过动态代理，极大简化了调用过程。

相比于静态代理， 动态代理的优势在于可以很方便的对代理类的函数进行统一的处理，而不用修改每个代理类的函数
"""

import urllib.request as request
import json


def fetch_resource(resource_id):
    """对于每一个REST操作，都会有类似的代码。差别仅在于API的地址和HTTP method（GET、POST、等）。
    此时，可以引入一个GetProxy，可以代替我们实现这些繁杂的工作。"""
    opener = request.urlopen('http://remote.server/api/resource/' + resource_id)
    if opener.code != 200:
        raise RuntimeError('invalid return code!')
    content = opener.read()
    try:
        return json.loads(content)
    except ValueError:
        return content


class GetProxy(object):
    def __getattr__(self, api_path):
        def _rest_fetch(*paras):
            print(paras)
            opener = request.urlopen('http://remote.server/api/' + api_path + '/' + '/'.join(paras))
            if opener.code != 200:
                raise RuntimeError('invalid return code!')
            content = opener.read()
            try:
                return json.loads(content)
            except ValueError:
                return content

        return _rest_fetch


if __name__ == "__main__":
    proxy = GetProxy()

    # 调用API
    proxy.user("123")  # http://remote.server/api/user/123
    proxy.resource('switch', "456")  # http://remote.server/api/resource/switch/456