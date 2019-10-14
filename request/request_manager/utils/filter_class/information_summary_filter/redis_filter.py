import redis
from . import BaseFilter


class RedisFilter(BaseFilter):
    """基于redis的持久化存储的去重判断依据的实现"""

    def _is_exists(self, hash_value):
        """判断redis对应的无序集合中是否有对应的数据"""
        return self.storage.sismember(self.redis_key, hash_value)

    def _save(self, hash_value):
        """
        利用redis无序集合进行存储
        :param hash_value:
        :return:
        """
        return self.storage.sadd(self.redis_key, hash_value)

    def _get_storage(self):
        """返回一个redis链接对象"""
        pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, db=self.redis_db)
        client = redis.StrictRedis(connection_pool=pool)
        return client
