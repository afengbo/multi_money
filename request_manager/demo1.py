from request_manager.request_filter import RequestFilter
from request_manager.utils.filter_class import get_filter_class
from request_manager.request import Request

r1 = Request("https://www.baidu.com/s?wd=go&wd=python")
r1.name = 'r1'
r2 = Request("https://www.baidu.com/s?wd=python&wd=go", query={'wd': 'python'})
r2.name = 'r2'
# r3 = Request("HTTPS://www.baidu.com/s?wd=python")
# r3.name = 'r3'
# r4 = Request("https://www.baidu.com/S?wd=python")
# r4.name = 'r4'
r_s = [r1, r2]

filter_obj = get_filter_class("memory")()

request_filter = RequestFilter(filter_obj)

for r in r_s:
    if request_filter.is_exists(r):
        print("请求重复：", r.name)
    else:
        # 处理请求
        fp = request_filter.mark_request(r)
        print("标记请求队形：", r.name, fp)

