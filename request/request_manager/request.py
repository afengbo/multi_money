# 构建一个请求对象


class Request(object):
    def __init__(self, url, method="GET", query={}, body={}):
        self.url = url
        self.method = method
        if not isinstance(query, dict):
            raise Exception("query must be a dict.")
        self.query = query
        if not isinstance(body, dict):
            raise Exception("body must be a dict.")
        self.body = body
