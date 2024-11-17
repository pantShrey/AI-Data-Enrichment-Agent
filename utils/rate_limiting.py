from ratelimit import limits, sleep_and_retry

# Constants for rate limiting
CALLS_PER_MINUTE = 30  # Default calls per minute, adjust as needed

@sleep_and_retry
@limits(calls=CALLS_PER_MINUTE, period=60)
def rate_limited_function():
    """
    Decorator to enforce rate limits on API calls.
    Replace the contents of this function with your API call logic.
    """
    pass  # Replace with the actual API logic

def rate_limit_decorator(calls_per_minute):
    """
    Factory function for creating rate limit decorators with custom limits.

    Args:
        calls_per_minute (int): The number of allowed calls per minute.

    Returns:
        function: A decorator function for rate limiting.
    """
    def decorator(func):
        @sleep_and_retry
        @limits(calls=calls_per_minute, period=60)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decorator
