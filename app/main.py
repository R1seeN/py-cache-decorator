from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:
        if data.get(args) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data[args] = result

            return result
        else:
            print("Getting from cache")

        return data.get(args)
    return wrapper
