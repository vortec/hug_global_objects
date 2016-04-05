import os


# As per 12 factor app, pass the configuration via
# environment variables.
# Other options could be JSON, ZooKeeper, etcd, hardcoded, ...


POSTGRES = {
    'host': os.environ.get('PGHOST', None),
    'port': int(os.environ.get('PGPORT', 5432)),
    'user': os.environ.get('PGUSER', None),
    'password': os.environ.get('PGPASSWORD', None),
    'database': os.environ.get('PGDATABASE', None)
}

REDIS = {
    'host': os.environ.get('REDIS_HOST', 'localhost'),
    'port': int(os.environ.get('REDIS_PORT', 6379)),
    'db': int(os.environ.get('REDIS_DB', 0))
}
