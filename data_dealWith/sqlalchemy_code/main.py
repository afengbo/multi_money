from sqlalchemy.orm import sessionmaker

from data_dealWith.douban.data_type4 import DoubanBook
from .models import engine, BigTag, SmallTag, Book, BookToTag


Session = sessionmaker(bind=engine)
spider = DoubanBook(20)


def store_tag_data():
    session = Session()
    for bt, st in spider.get_tags():
        if not session.query(BigTag).filter_by(btag=bt[0]).first():    # 判断，避免重复数据入库
            big_tag = BigTag(btag=bt[0])
            session.add(big_tag)
            session.commit()    # 因为后面需要用big_tag的id，所以这里必须先commit一次
            for t in st:
                small_tag = SmallTag(stag=t, btag_id=big_tag.id)
                session.add(small_tag)
    session.commit()
    session.close()


def store_detail_data():
    session = Session()
    for t in session.query(SmallTag).all():    # 查询小标签出来，逐个下载
        for page, url_list in spider.get_all_pages(t.stag):   # 获取所有翻页
            for book_url in url_list:    # 遍历列表页
                detail = spider.get_book_detail(book_url)
                detail = spider.clean_detail(detail)    # 清洗数据
                book = Book(**detail)
                session.add(book)
            break
        break
    session.commit()
    session.close()


if __name__ == '__main__':
    store_tag_data()
    store_detail_data()
