import requests
import lxml.etree

class DoubanBook(object):

    # 书列表，根据tag名称和offset 20
    book_list_from_tag_url = "https://book.douban.com/tag/{tag_name}?start={offset}&type=T"

    def get_one_page(self, tag_name, offset):
        '''获取书籍详情页地址'''
        response = requests.get(self.book_list_from_tag_url.format(tag_name=tag_name, offset=offset))
        html = lxml.etree.HTML(response.content)
        book_url_list = html.xpath("//ul[@class='subject-list']/li/div[@class='pic']/a/@href")
        return book_url_list

if __name__ == '__main__':
    spider = DoubanBook()
    url_list = spider.get_one_page("小说", 0)
    url_list2 = spider.get_one_page("小说", 980)
    url_list3 = spider.get_one_page("小说", 1000)    # 超过1000没有数据
    print(url_list)
    print(url_list2)
    print(url_list3)
