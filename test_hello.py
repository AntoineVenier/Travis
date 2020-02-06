import pytest

def hello(name):
    return 'Hello ' + name

class test:
    def test_hello(self):
        assert hello('Celine') == 'Hello Celine'




 