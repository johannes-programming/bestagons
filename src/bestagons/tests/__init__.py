import unittest

__all__ = ["test"]


def test():
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="bestagons.tests")
    runner = unittest.TextTestRunner()
    result = runner.run(tests)
    return result
