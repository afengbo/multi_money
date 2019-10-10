# test redis_queue

from request_manager.utils.redis_tools import get_redis_queue_cls

Queue = get_redis_queue_cls("priority")

REDIS_QUEUE_CONFIG = {
    "name": "pqueue",
    "host": "172.17.0.2",
    "db": 15,
    "use_lock": False,
    "redis_lock_config": {
        "lock_name": "pqueue_lock",
        "host": '172.17.0.2'
    }
}

pqueue = Queue(**REDIS_QUEUE_CONFIG)
pqueue.put({"value10": 10})
print(pqueue.get())
