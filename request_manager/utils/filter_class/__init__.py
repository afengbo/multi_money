

def get_filter_class(cls_name):
    """返回对应的过滤器类对象"""
    if cls_name == "bloom":
        from .bloom_filter.bloom_redis import BloomFilter
        return BloomFilter
    elif cls_name == "memory":
        from .information_summary_filter.memory_filter import MemoryFilter
        return MemoryFilter
    elif cls_name == "mysql":
        from .information_summary_filter.mysql_filter import MysqlFilter
        return MysqlFilter
    elif cls_name == "redis":
        from .information_summary_filter.redis_filter import RedisFilter
        return RedisFilter
