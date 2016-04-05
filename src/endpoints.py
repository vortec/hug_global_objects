import directives
import hug

@hug.get('increase')
def increase(redis: directives.redis, amount: hug.types.number=1):
    redis.incr('counter', amount)
    return redis.get('counter')
