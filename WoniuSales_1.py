#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.client
from random import random

class WoniuSalesTest:
    def __init__(self):
        self.conn = http.client.HTTPConnection(host='192.168.80.128', port=8080)
        self.header = {'Content-Type':'application/x-www-form-urlencoded'}
        self.cookie = ''

    def access_homepage(self):
        self.conn.request(method='GET', url='/woniusales/')
        resp = self.conn.getresponse().read().decode()
        # print(resp)
        if '蜗牛进销存-首页' in resp:
            print('测试成功')
        else:
            print('测试失败')

    def do_login(self):
        body = 'username=admin&password=admin123&verifycode=0000'
        self.conn.request(method='POST', url='/woniusales/user/login', body=body, headers=self.header)
        resp = self.conn.getresponse()
        self.cookie += resp.getheader('Set-Cookie')
        # print(self.cookie)
        if resp.read().decode() == 'login-pass':
            print("登录成功")
        else:
            print("登录失败")


if __name__ == '__main__':
    test = WoniuSalesTest()
    test.access_homepage()
    test.do_login()
    # test.add_customer()


# 接口测试销售出库



