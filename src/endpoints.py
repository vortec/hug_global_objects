import directives
import hug


# Endpoints use the directive and the io object directly, so that
# unit testing those things will be a lot easier.
# This way you can just pass your testing connection or a mock into
# the endpoint.

@hug.get('increase')
def increase(redis: directives.redis, amount: hug.types.number=1):
    redis.incr('counter', amount)
    return redis.get('counter')
