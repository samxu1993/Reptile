# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: wechat_password.py
# @Author: SamXss
# @Institution: --- University, ---, China
# @E-mail: SamXss0101@gmail.com
# @Site: 
# @Time: 12月 02, 2021
# ---
import execjs
# 1.实例化一个node对象
node =execjs.get()

# 2.js源文件编译
ctx=node.compile(open("./wechat.js",encoding="utf-8").read())

# 3.执行js函数
funcName="getPwd('{0}')".format('a55220012')
pwd=ctx.eval(funcName)
print(pwd)