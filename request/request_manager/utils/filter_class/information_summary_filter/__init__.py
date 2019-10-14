# 信息摘要hash算法去重方案实现
# 1. 普通内存版本
# 2. Redis持久化版本
# 3. MySQL持久化版本

import six
import hashlib


class BaseFilter(object):
    """基于信息摘要算法进行数据去重判断和存储"""
    def __init__(self, hash_func_name="md5", redis_host='localhost', redis_port=6379, redis_db=0, redis_key='filter', mysql_url=None, mysql_table_name="filter"):
        # redis配置
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_key = redis_key

        self.mysql_url = mysql_url
        self.mysql_table_name = mysql_table_name

        self.hash_func = getattr(hashlib, hash_func_name)
        self.storage = self._get_storage()

    def _safe_data(self, data):
        """
        python2 str == python bytes
        python2 unicode == python3 str
        :param data: 给定的原始数据
        :return: 二进制类型的字符串数据
        """
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception("Please input string")
        elif six.PY2:
            if isinstance(data, str):
                return data
            elif isinstance(data, unicode):
                return data.encode()
            else:
                raise Exception("Please input string")

    def _get_hash_value(self, data):
        """
        根据给定数据，返回对应信息摘要hash值
        :param data: 给定的原始数据
        :return: hash值
        """
        hash_obj = self.hash_func()
        hash_obj.update(self._safe_data(data))
        hash_value = hash_obj.hexdigest()
        return hash_value

    def save(self, data):
        """
        根据data算出指纹进行存储
        :param data: 给定的原始数据
        :return: 存储的hash_value
        """
        hash_value = self._get_hash_value(data)
        self._save(hash_value)
        return hash_value

    def _save(self, hash_value):
        """
        存储对应的hash值（方法由子类重写）
        :param data: 通过摘要算法算出的hash值
        :return: 存储结果
        """
        pass

    def is_exists(self, data):
        """
        判断给定的指纹是否存在
        :param data: 给定的指纹信息
        :return: True or False
        """
        hash_value = self._get_hash_value(data)
        return self._is_exists(hash_value)

    def _is_exists(self, hash_value):
        """
        判断指纹是否存在（方法由子类重写）
        :param data: 通过摘要算法算出的hash值
        :return: True or False
        """
        pass

    def _get_storage(self):
        """
        存储（方法由子类重写）
        :return:
        """
        pass
