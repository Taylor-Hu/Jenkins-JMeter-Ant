#!/usr/bin/env python
#-*- coding:utf-8 -*-

# from protocol.python单元测试.function import Function
import unittest

# unittest当中，所有的测试用例方法，必须以test开头
# 所有的测试用例按照方法名进行排序确定运行顺序
# 必须调用类方法setUpClass进行初始化，不能使用__init__构造方法

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
    # def __init__(self):
    #     self.function = Function()

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
    unittest.main()


# 初始化。。。
# 每一个测试用例运行前调用
# test_checknum_01
# 每一个测试用例运行完后调用
# 每一个测试用例运行前调用
# test_checknum_10
# 每一个测试用例运行完后调用
# 每一个测试用例运行前调用
# test_checknum_02
# 每一个测试用例运行完后调用
# 每一个测试用例运行前调用
# test_checknum_03
# 每一个测试用例运行完后调用
# 结束调用。。。