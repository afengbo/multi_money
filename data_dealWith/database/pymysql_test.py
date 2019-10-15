import pymysql.cursors


class PyMysqlBaseUsage(object):

    def __init__(self,
                 host='192.168.33.6',
                 port=3306,
                 user='root',
                 password='333333',
                 db='test_db',
                 charset='utf8mb4',
                 cursorclass=pymysql.cursors.DictCursor):

        # 连接到数据库
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset,
            cursorclass=cursorclass)
        print("已建立数据库连接")

    def create_table(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()

    def drop_table(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()

    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
        self.connection.commit()

    def select_all(self, sql, params=None):
        results = None
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            results = cursor.fetchall()
        return results

    def select_many(self, sql, params=None, size=1):
        results = None
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            results = cursor.fetchmany(size)
        return results

    def select_one(self, sql, params=None):
        result = None
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchone()
        return result

    def table_exist(self, database_name, table_name, params=None):
        table_exist_sql = '''SHOW TABLES FROM %s;''' % database_name
        with self.connection.cursor() as cursor:
            cursor.execute(table_exist_sql, params)
            result = cursor.fetchall()
        table_list = [t['Tables_in_%s' % database_name] for t in result]
        if table_name in table_list:
            return True
        else:
            return False

    def __del__(self):
        self.connection.close()
        print("已断开数据库连接")


if __name__ == '__main__':
    obj = PyMysqlBaseUsage(host="192.168.33.6", user="root", password="333333", db="test_db")
    # 判断表是否存在
    # res = obj.table_exist(database_name='test_db', table_name='test_table2')
    # if res:
    #     print("该表已存在,不可创建同名表!")
    # else:
    #     # 建表语句
    #     create_sql = '''
    #         CREATE TABLE `test_table2` (
    #             `id` int(11) NOT NULL AUTO_INCREMENT,
    #             `colume1` varchar(255) NOT NULL,
    #             `colume2` varchar(255) NOT NULL,
    #             PRIMARY KEY (`id`)
    #         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    #         AUTO_INCREMENT=1;'''
    #     obj.create_table(create_sql)

    # 删表语句
    # drop_sql = '''DROP TABLE test_table'''
    # obj.drop_table(drop_sql)

    # 插入数据
    # insert_sql = "INSERT INTO `test_table` (`colume1`, `colume2`) VALUES (%s, %s)"
    # obj.insert(insert_sql, ("data3", "data4"))

    # 查询数据
    # select_sql = "SELECT * FROM `test_table`"
    # results = obj.select_all(select_sql)
    # print("all: ", results)
    #
    # results = obj.select_many(select_sql, size=10)
    # print("many: ", results)
    #
    # result = obj.select_one(select_sql)
    # print("one: ", result)
