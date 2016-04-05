import psycopg2
import redis


# Helper functions which can be used in the tests and from app.py

def make_redis(**kwargs):
    return redis.StrictRedis(**kwargs)
