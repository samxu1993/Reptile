# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: jd.py
# @Author: SamXss
# @Institution: --- University, ---, China
# @E-mail: SamXss0101@gmail.com
# @Site: 
# @Time: 12月 02, 2021
# ---
from execjs import get as execjs_get
from requests import get
from lxml import etree

# 1.获取pubKey
url = "https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
response_text = get(url, headers=headers).text
tree = etree.HTML(response_text)
pubKey = tree.xpath('//input[@id="pubKey"]/@value')[0]

# 2. 实例化一个node对象
node = execjs_get()

# 3. js源文件编译
ctx = node.compile(open('./jd.js', encoding='utf-8').read())

# 4. 执行js函数
funcName = 'getPwd("{0}","{1}")'.format('123123123', pubKey)
pwd = ctx.eval(funcName)
print(pwd)
