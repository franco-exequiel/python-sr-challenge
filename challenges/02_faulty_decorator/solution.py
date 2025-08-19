from functools import wraps

# --- START YOUR SOLUTION HERE ---
# Implement a decorator factory `limit_calls(max_calls)`.
# Each decorated function must enforce its own call limit.
# Placeholder (incorrect): shared counter.

def limit_calls(max_calls: int):
    def decorator(func):
        #Contadores
        calls = 0 
        instance_calls = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls, instance_calls
            if args and hasattr(args[0], func.__name__):
                inst = args[0]
                if inst not in instance_calls:
                    instance_calls[inst] = 0
                if instance_calls[inst] >= max_calls:
                    raise ValueError(f"Limit of {max_calls} calls exceeded for {func.__name__}")
                instance_calls[inst] += 1

            else:
                if calls >= max_calls:
                    raise ValueError(f"Limit of {max_calls} calls exceeded for {func.__name__}")
                calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
# --- END OF YOUR SOLUTION ---
