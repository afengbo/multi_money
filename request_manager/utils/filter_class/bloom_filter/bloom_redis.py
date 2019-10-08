# 布隆过滤器 redis存储hash值
import redis

from multi_hash import MultiHash


class BloomFilter(object):
    """
    布隆过滤器 redis存储hash值
    salts在同一个项目中不能更改
    """
    def __init__(self, salts, redis_host='localhost', redis_port=6379, redis_db=0, redis_key='filter'):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_key = redis_key
        self.client = self._get_storage()
        self.multi_hash = MultiHash(salts)

    def _get_storage(self):
        """返回一个redis链接对象"""
        pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, db=self.redis_db)
        client = redis.StrictRedis(connection_pool=pool)
        return client

    def save(self, data):
        """将原始数据在hash表中一一映射，返回对应的偏移量"""
        hash_values = self.multi_hash.get_hash_value(data)
        offsets = []
        for hash_value in hash_values:
            offset = self._get_offset(hash_value)
            offsets.append(offset)
            self.client.setbit(self.redis_key, offset, 1)
        return offsets

    def is_exists(self, data):
        """判断是否存在"""
        hash_values = self.multi_hash.get_hash_value(data)
        for hash_value in hash_values:
            offset = self._get_offset(hash_value)
            res = self.client.getbit(self.redis_key, offset)
            if res == 0:
                return False
        return True

    def _get_offset(self, hash_value):
        """
        求余
        2**8 = 256
        2**20 = 1024 * 1024
        (2**8 * 2**20 * 2**3)      代表hash表的长度，在同一个项目中不能更改
        """
        return hash_value % (2**8 * 2**20 * 2**3)


if __name__ == '__main__':
    data = ['1', '2', '3', '4', '1', 'a', '中文', 'a', '中']
    bf = BloomFilter(['1', '22', '333'], redis_host='172.17.0.2')
    for d in data:
        if not bf.is_exists(d):
            bf.save(d)
            print("映射数据成功：", d)
        else:
            print("重复数据：", d)
