import unittest

def hello(name):
    return 'Hello ' + name


class Test(unittest.TestCase):
    def test_hello(self):
        assert hello('Celine') == 'Hello Celine'

unittest.main()



