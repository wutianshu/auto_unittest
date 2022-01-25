import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestClass2 setup')

    @classmethod
    def tearDownClass(cls):
        print('TestClass2 teardown')

    def setUp(self):
        print('method setup')

    def tearDown(self):
        print('method teardown')

    def test_class2_method1(self):
        self.assertEquals(1, 1)

    def test_class2_method2(self):
        self.assertTrue(1 in [1, 2, 3])

    def test_class2_method3(self):
        self.assertTrue(1 in [2, 3, 4])
