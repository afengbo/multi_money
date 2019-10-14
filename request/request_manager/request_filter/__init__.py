# 实现请求去重逻辑
import urllib.parse


class RequestFilter(object):
    def __init__(self, filter_obj):
        self.filter_obj = filter_obj

    def is_exists(self, request_obj):
        """判断请求是否已经处理"""
        data = self._get_request_filter_data(request_obj)
        return self.filter_obj.is_exists(data)

    def mark_request(self, request_obj):
        """
        标记已经处理过的请求对象
        return: 标记
        """
        data = self._get_request_filter_data(request_obj)
        return self.filter_obj.save(data)

    def _get_request_filter_data(self, request_obj):
        """
        根据一个请求对象处理数据，转换为字符串，然后再进行去重处理
        :param request_obj:
        :return:转换后的字符串
        """
        # 1. url的处理
        # 把协议和域名部分进行大小写统一，其他的保留原始大小写格式
        url = request_obj.url
        _ = urllib.parse.urlparse(url)
        url_no_query = _.scheme + "://" + _.hostname + _.path
        # 对查询参数进行简单的排序
        url_query = urllib.parse.parse_qsl(_.query)

        # 2. method处理：对请求方法置为统一大写 .upper()
        method = request_obj.method.upper()

        # 3. query处理：把URL中的请求查询参数和query里的进行合并
        query = request_obj.query.items()
        str_query = str(set(sorted(list(query) + url_query)))
        # print(str_query)

        # 4. body处理：排序后转换为字符串   str(sorted({}.items()))
        str_body = str(sorted(request_obj.body.items()))

        data = url_no_query + method + str_query + str_body
        return data

