# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: steam_password.py
# @Author: SamXss
# @Institution: --- University, ---, China
# @E-mail: SamXss0101@gmail.com
# @Site: 
# @Time: 12月 02, 2021
# ---
# 1.获取密钥
import requests
import execjs

url="https://store.steampowered.com/login/getrsakey/"
data={
    "donotcache":"1638422411300",
    "username":"123123@qq.com"
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
respose_json=requests.post(url,headers=headers,data=data).json()
exp=respose_json["publickey_exp"]
mod=respose_json["publickey_mod"]
# print(mod)
# print(exp)

# 2.进行密码逆向
node=execjs.get()
ctx=node.compile(open("./steam.js",encoding="utf-8").read())

funcName="getPwd('{}','{}','{}')".format("123456",mod,exp)
pwd=ctx.eval(funcName)
print(pwd)
