from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_two_with_kwargs(a: int, b: int, *, c: str, d: bool) -> int:
    return a + b


def test_positive_case_args_only():
    assert sum_two(1, 2) == 3

def test_positive_case_with_kwargs():
    assert sum_two_with_kwargs(1, 2, c='str', d=True) == 3

def test_raise_type_error():
    try:
        sum_two(1, '2')
    except TypeError:
        pass
    else:
        raise AssertionError(
            'Test passed, but TypeError exception was expected'
        )

def test_raise_type_error_with_kwargs():
    try:
        sum_two_with_kwargs(1, 2, c=False, d='str')
    except TypeError:
        pass
    else:
        raise AssertionError(
            'Test passed, but TypeError exception was expected'
        )


if __name__ == '__main__':
    test_positive_case_args_only()
    test_positive_case_with_kwargs()
    test_raise_type_error()
    test_raise_type_error_with_kwargs()
