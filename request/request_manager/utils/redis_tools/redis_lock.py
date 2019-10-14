import pickle
import redis
import threading
import socket
import os


class RedisLock(object):
    def __init__(self, lock_name, host='localhost', port=6379, db=0):
        self.redis = redis.StrictRedis(host=host, port=port, db=db)
        self.lock_name = lock_name

    def _get_thread_id(self):
        thread_id = socket.gethostname() + str(os.getpid()) + threading.current_thread().name
        return thread_id

    def acquire_lock(self, thread_id=None, expire=10, block=True):
        """
        :param thread_id: 表明每个线程的唯一标识值，用来判断解锁
        :param expire: 锁过期时间
        :return:
        """
        if thread_id is None:
            thread_id = self._get_thread_id()

        while block:
            # 如果lock_name 存在，ret=0，否则ret=1
            ret = self.redis.setnx(self.lock_name, pickle.dumps(thread_id))
            if ret == 1:
                self.redis.expire(self.lock_name, expire)
                print("上锁成功")
                return True

        # 如果lock_name 存在，ret=0，否则ret=1
        ret = self.redis.setnx(self.lock_name, pickle.dumps(thread_id))
        if ret == 1:
            self.redis.expire(self.lock_name, expire)
            print("上锁成功")
            return True
        else:
            print("上锁失败")
            return False

    def release_lock(self, thread_id=None):
        if thread_id is None:
            thread_id = self._get_thread_id()
        ret = self.redis.get(self.lock_name)
        # print(ret, '*'*8, thread_id)
        # 确保解锁线程还是上锁线程
        if ret is not None and pickle.loads(ret) == thread_id:
            self.redis.delete(self.lock_name)
            print("解锁成功")
            return True
        else:
            print("解锁失败")
            return False


if __name__ == '__main__':
    redis_lock = RedisLock("redis_lock", host="172.17.0.2")

    if redis_lock.acquire_lock():
        print("执行相应操作")
        redis_lock.release_lock()
