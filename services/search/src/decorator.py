import os
from functools import wraps

from dotenv import load_dotenv
from flask_caching import Cache

load_dotenv("config.env")

cache = Cache()


def init_cache(app):
    app.config['CACHE_TYPE'] = os.getenv('CACHE_TYPE', 'RedisCache')
    app.config['CACHE_REDIS_HOST'] = os.getenv('CACHE_REDIS_HOST', 'localhost')
    app.config['CACHE_REDIS_PORT'] = int(os.getenv('CACHE_REDIS_PORT', 6379))
    app.config['CACHE_DEFAULT_TIMEOUT'] = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 120))
    cache.init_app(app)


def cache_redis(timeout=300, key_prefix=''):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key_prefix + ":" + str(kwargs)
            print(cache_key)
            cached_result = cache.get(cache_key)
            print(cached_result)
            if cached_result is not None:
                return cached_result

            result = f(*args, **kwargs)
            cache.set(cache_key, result, timeout=timeout)
            return result

        return decorated_function

    return decorator
