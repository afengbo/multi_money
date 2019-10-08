import hashlib

import six

# 1. 多个hash函数的实现和求值
# 2. hash表实现和实现对应的映射和判断


class MultiHash(object):
    """根据提供的原始数据和的预定义的多个salt，生成多个hash函数值"""
    def __init__(self, salts, hash_func_name="md5"):
        self.salts = salts
        if len(salts) < 3:
            raise Exception("Please provide at least 3 values...")
        self.hash_func = getattr(hashlib, hash_func_name)

    def get_hash_value(self, data):
        """根据提供的原始数据，返回多个hash值"""
        hash_value = []
        for i in self.salts:
            hash_obj = self.hash_func()
            hash_obj.update(self._safe_data(data))
            hash_obj.update(self._safe_data(i))
            ret = hash_obj.hexdigest()
            hash_value.append(int(ret, 16))
        return hash_value

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


if __name__ == '__main__':
    mh = MultiHash(['1', '2', '3'])
    print(mh.get_hash_value('fone'))
