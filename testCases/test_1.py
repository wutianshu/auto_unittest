import unittest
from parameterized import parameterized, param
from ddt import data, unpack, ddt

@ddt
class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestClass1 setup')

    @classmethod
    def tearDownClass(cls):
        print('TestClass1 teardown')

    def setUp(self):
        print('method setup')

    def tearDown(self):
        print('method teardown')

    @parameterized.expand([param(1, 1, 2), param('hello', ' world', 'hello world')])
    def test_class1_method1(self, first, second, result):
        self.assertEqual(first + second, result)

    @data(1, 2, 3)
    def test_class1_method2(self, first):
        self.assertTrue(first in [1, 2, 3])

    @data([1, 2, 3], [2, 4, 6])
    @unpack
    def test_class1_method3(self, first, second, result):
        self.assertEqual(first + second, result)
