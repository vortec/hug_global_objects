class IOStates:
    """
    Singleton class with immutable attributes, supposed to store global
    database connection objects. This class makes sure that:

     * connection objects are globally accessible once initialized
     * some other place must do the initial connection setup (probably
       the controller, aka app.py)
     * requests for connection objects are rejected until the other
       place has passed those objects into here
     * once passed objects cannot be replaced, as we have no control
       over anything. ie., endpoints could keep a reference and keep
       using the old ones which leads to states we don't want to have.

    Once you get disconnected from your database, the entire process
    should crash. The reasoning behind that is that once that situation
    occurs, something bad is going on in your distributed system which
    cannot be fixed by your application server by any means. So the best
    possible way to deal with a network outage or similar is to stop
    functioning completely and let your container orchestration system
    or sysadmin fix the real problem first.

    This class assists you in following that philosophy, but does not
    know about the real states of your connections.
    """
    __initialized = False
    __redis = None

    def __init__(self):
        self.__initialized = False

    def initialize(self, redis):
        self.__redis = redis
        self.__initialized = True

    @property
    def initialized(self):
        return self.__initialized

    @property
    def redis(self):
        if not self.initialized:
            raise IOStatesNotInitializedError()
        return self.__redis


class IOStatesNotInitializedError(Exception):
    pass


# Construct class so that other modules can keep a reference to it.
# It's not ready to use yet, initialize() must be called first!
io = IOStates()
