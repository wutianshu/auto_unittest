import HTMLTestRunner
import time, os
import unittest
from testCases.test_1 import TestClass1
from testCases.test_2 import TestClass2

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    case_path = os.path.join(os.getcwd())
    report_path = os.path.join(os.getcwd(), 'report')
    report_abs_path = os.path.join(report_path, 'result.html')

    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestClass1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestClass2))

    with open(report_abs_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='自动化测试报告', description='用例执行情况：')
        runner.run(suite)
