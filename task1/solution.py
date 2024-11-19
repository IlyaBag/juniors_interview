from typing import Any, Callable


def strict(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        annots = func.__annotations__

        for arg, annot_name in zip(args, annots):
            if type(arg) != annots[annot_name]:
                raise TypeError(
                    f"Parameter '{annot_name}' has wrong type {type(arg)}, "
                    f"expected {annots[annot_name]}"
                )


        for kwarg_name in kwargs:
            if type(kwargs[kwarg_name]) != annots[kwarg_name]:
                raise TypeError(
                    f"Parameter '{kwarg_name}' has wrong type "
                    f"{type(kwargs[kwarg_name])}, expected {annots[kwarg_name]}"
                )

        result = func(*args, **kwargs)
        return result
    return inner
