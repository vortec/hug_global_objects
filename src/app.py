import config
import connections
import endpoints
import hug
from io_states import io


redis_connection = connections.make_redis(**config.REDIS)

io.initialize(redis_connection)

@hug.extend_api('/')
def api():
    return [endpoints]
