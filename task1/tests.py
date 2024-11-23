import unittest

from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_two_with_kwargs(a: int, b: int, *, c: str, d: bool) -> int:
    return a + b


class TestStrict(unittest.TestCase):
    """Test decorator '@strict' with two functions that accept positional only
    and positional and keyword arguments."""

    def test_positive_case_args_only(self):
        self.assertTrue(sum_two(1, 2) == 3)

    def test_positive_case_with_kwargs(self):
        self.assertTrue(sum_two_with_kwargs(1, 2, c='string', d=True) == 3)

    def test_raise_type_error(self):
        self.assertRaises(TypeError, sum_two, 1, '2')

    # Different usecases of 'assertRaises*' are used only for demonstration
    def test_raise_type_error_with_kwargs(self):
        with self.assertRaisesRegex(
            TypeError,
            "Parameter 'd' has wrong type <class 'str'>, expected <class 'bool'>"
        ):
            sum_two_with_kwargs(1, 2, c='string', d='string too')


if __name__ == '__main__':
    unittest.main()
