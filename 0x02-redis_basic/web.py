import requests
import redis
import time
from functools import wraps

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Decorator for caching
def cache_expiring(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            key = f'cache:{url}'
            cached_result = redis_client.get(key)
            if cached_result:
                return cached_result.decode('utf-8')
            else:
                result = func(url)
                redis_client.setex(key, seconds, result)
                return result
        return wrapper
    return decorator

# Actual function to get the page content
@cache_expiring(10)
def get_page(url):
    # Track URL access count
    count_key = f'count:{url}'
    redis_client.incr(count_key)

    # Get page content
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(url))  # This should take a few seconds to load due to the simulated delay
    time.sleep(5)  # Sleep to allow cache to expire
    print(get_page(url))  # This should load instantly due to cache
