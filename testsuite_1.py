import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
# from protocol.python单元测试.unittest_01 import UnitTest01
# from protocol.python单元测试.send_mail import Send_Email
from send_mail import Send_Email

class Function:
    def check_number(self, str):
        is_point = 0
        is_separator = 0
        is_digital = 0
        is_correct = False

        for i in str:
            num = ord(i)
            if num == 47 or num < 45 or num > 57:
                raise Exception("ERROR-NUMBER")
            elif num == 45:
                is_separator += 1
            elif num == 46:
                is_point += 1
            else:
                is_digital += 1

        # 负号、小数点有且仅有一个，而且必须有一个数字
        if is_separator <= 1 and is_point <= 1 and is_digital > 0:
            # 负号必须写在最前面
            if is_separator == 1 and ord(str[0]) != 45:
                is_correct = False
            else:
                is_correct = True
        else:
            is_correct = False

        return is_correct

class UnitTest02(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.function = Function()
    #     print("初始化。。。")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.function = None
    #     print("结束调用。。。")
    #
    # # 非类级初始化方法，会在每一个测试用例执行前运行一次
    # def setUp(self):
    #     print("每一个测试用例运行前调用")
    #
    # def tearDown(self):
    #     print("每一个测试用例运行完后调用")

    def test_checknum_1(self):
        function = Function()
        self.assertEqual(function.check_number("12345"), True)
        print("test_checknum_01")

    def test_checknum_2(self):
        function = Function()
        self.assertEqual(function.check_number("12.345"), True)
        print("test_checknum_02")

    def test_checknum_3(self):
        function = Function()
        self.assertEqual(function.check_number("-345"), True)
        print("test_checknum_03")

    def test_checknum_10(self):
        function = Function()
        self.assertEqual(function.check_number(""), False)
        print("test_checknum_10")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest02))

    # 很重要：拼接的时候%H:%M:%S会存在识别不到":"的问题
    # filename = time.strftime('%Y-%m-%d_%H:%M:%S.csv')
    now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    report = os.path.join(os.path.abspath('.'), 'report')
    if not os.path.exists(report):
        os.mkdir(report)

    filename = 'woniusales_test_report_%s.html'% now
    HtmlFile = os.path.join(report, filename)
    runner = HTMLTestRunner(stream=open(HtmlFile, 'wb'), title='测试报告', description='这是一个牛逼的报告')
    runner.run(suite)

    # 发送邮件
    se = Send_Email()
    se.email('test', HtmlFile, filename)
