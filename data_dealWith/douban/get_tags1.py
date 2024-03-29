import requests
import lxml.etree


class DoubanBook(object):
    # 标签列表页
    tag_list_url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-hot"

    def get_tags(self):
        """获取tag信息"""
        response = requests.get(self.tag_list_url)
        html = lxml.etree.HTML(response.content)
        for div in html.xpath("//div[@class='article']/div[2]/div"):
            big_tag = div.xpath("./a/@name")
            small_tags = div.xpath("./table//td/a/text()")
            print(big_tag)
            print(small_tags)


if __name__ == '__main__':
    spider = DoubanBook()
    spider.get_tags()
