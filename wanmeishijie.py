# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: wanmeishijie.py
# @Author: SamXss
# @Institution: --- University, ---, China
# @E-mail: SamXss0101@gmail.com
# @Site: 
# @Time: 12月 02, 2021
# ---
import requests
from lxml import etree
import execjs
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

# 发起请求获取公钥
url="https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f"
page_text=requests.get(url,headers=headers).text
tree=etree.HTML(page_text)
key=tree.xpath("//input[@id='e']/@value")[0]


# 加密逆向
node=execjs.get()
ctx=node.compile(open("./wanmeishijie.js",encoding="utf-8").read())
funcname="getPwd('{}','{}')".format("123456",key)

pwd=ctx.eval(funcname)
print(pwd)