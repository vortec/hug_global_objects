from io_states import io
import hug


@hug.directive()
def redis(**kwargs):
    return io.redis
