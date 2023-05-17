import unittest

from demo.demo import demo


class TestDemo(unittest.TestCase):
    def test_demo(self):
        self.assertEquals(demo('Richard'),'Hello Richard')


if __name__ == '__main__':
    unittest.main()