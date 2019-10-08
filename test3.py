# test redis_queue

from redis_queue.priority_redis_queue import PriorityRedisQueue

pqueue = PriorityRedisQueue("pqueue", host="172.17.0.2", db=15)
pqueue.put({"value10": 10})
print(pqueue.get(block=False))
