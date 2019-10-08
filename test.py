from request_manager.utils.filter_class.information_summary_filter.mysql_filter import MysqlFilter

# filt = MemoryFilter()
# redis_filter = RedisFilter(redis_host='172.17.0.4')
mysql_url = "mysql+pymysql://root:333333@172.17.0.5:3306/spider_data?charset=UTF8MB4"
mysql_filter = MysqlFilter(mysql_url=mysql_url, mysql_table_name='filter2')

data = ['1', '2', '3', '4', '1', 'a', '中文', 'a', '中']

for d in data:
    if mysql_filter.is_exists(d):
        print("重复数据剔除:", d)
    else:
        mysql_filter.save(d)
        print("已保存数据:", d)
