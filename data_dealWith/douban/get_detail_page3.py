import requests
import lxml.etree
import re

class DoubanBook(object):

    # book info中的所有字段
    book_info_details = ["作者", "出版社", "出品方", "原作名", "译者", "出版年", "页数", "定价", "装帧", "丛书", "ISBN", "副标题"]

    def get_book_detail(self, book_url):
        '''获取书籍详情'''
        response = requests.get(book_url)
        html = lxml.etree.HTML(response.content)
        # info内的标签没有规则，xpath很难定位
        info_text_list = html.xpath("//div[@id='info']//text()")
        # 使用正则来处理
        info_str = "".join(info_text_list)    # 全部拼接为字符串
        info_str = re.sub(r"\s", "", info_str)    # 剔除空白字符
        info_str = re.sub(r"\xa0", "", info_str)    # 剔除无用字符

        print(info_str)
        # 作者:[日]东野圭吾出版社:南海出版公司出品方:新经典文化原作名:ナミヤ雑貨店の奇蹟译者:李盈春出版年:2014-5页数:291定价:39.50元装帧:精装丛书:新经典文库·东野圭吾作品ISBN:9787544270878

        # 筛选出info中每一个字段的值
        for filed in self.book_info_details:
            # 挨个筛选出字段，如 '作者:[日]东野圭吾出版社'
            ret = re.search("%s:(.*?):" % filed, info_str + ":")
            if ret:
                # 剔除掉 '作者:[日]东野圭吾出版社'末尾的'出版社'，其他同理
                value = re.sub("(%s)$" % ("|".join(self.book_info_details)), "", ret.group(1))
                print(filed, ":", value)
            else:
                print(filed, ":", None)

        # 选取标题
        book_title = html.xpath("//div[@id='wrapper']/h1/span/text()")[0].strip()
        print("书名: ", book_title)

        # 评分：
        rating_num = html.xpath("//div[@id='interest_sectl']//strong/text()")[0].strip()
        print("评分: ", rating_num)

        # 内容简介
        book_summary = html.xpath("//div[@class='related_info']/div[@class='indent'][1]//div[@class='intro']//text()")
        print(book_summary)

        # 作者简介
        # 注意indent后面那个神奇的空格
        author_summary = html.xpath("//div[@class='related_info']/div[@class='indent ']//div[@class='intro']//text()")
        print(author_summary)

if __name__ == '__main__':
    book_url = "https://book.douban.com/subject/25862578/"

    spider = DoubanBook()
    spider.get_book_detail(book_url)
