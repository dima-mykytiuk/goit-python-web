import math
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def get_circumference(radius: int) -> float:
    circumference = 2 * math.pi * radius
    print('Func call')
    return circumference
