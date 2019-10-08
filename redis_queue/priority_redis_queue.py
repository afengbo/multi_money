import pickle

from .base import BaseRedisQueue


class PriorityRedisQueue(BaseRedisQueue):
    def qsize(self):
        self.last_qsize = self.redis.zcard(self.name)
        return self.last_qsize

    def put_nowait(self, obj):
        """
        :param obj: (score, value)
        :return:
        """
        if self.lazy_limit and self.last_qsize < self.maxsize:
            pass
        elif self.full():
            raise self.Full
        # print(type(pickle.dumps(obj[1])))
        self.last_qsize = self.redis.zadd(self.name, obj)
        return True

    def get_nowait(self):
        """
        0, 0 : 取权重最小的
        -1, -1 : 取权重最大的
        :return:
        """
        ret = self.redis.zrange(self.name, -1, -1)

        if not ret:
            raise self.Empty

        self.redis.zrem(self.name, ret[0])
        # return pickle.loads(ret)
        return ret
