# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: weibo.py
# @Author: SamXss
# @Institution: --- University, ---, China
# @E-mail: SamXss0101@gmail.com
# @Site: 
# @Time: 9月 26, 2021
# ---
import requests
import json


class Weibo:
    def __init__(self):
        """
        参数初始化
        :param self:
        :return:
        """
        self.url = "https://weibo.com/aj/photo/popview?"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            # 需要更改自己cookie
            "cookie":"xxx",
            "referer": "https://weibo.com/p/1006066269329742/photos?from=page_100606&mod=TAB",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
            "content-type":"application/x-www-form-urlencoded"
        }
        self.param  = {
            "ajwvr": 6,
            "mid": 4681820550989068,
            "pid": "006Qht3Ely1guhohhhmknj63gg56o4qt02",
            "uid": 6269329742,
            "type": 0,
            "page_id": 1006066269329742,
            "curclear_picSrc": "//wx4.sinaimg.cn/mw1024/006Qht3Ely1guhohhhmknj63gg56o4qt02.jpg",
            "pic_objects": "1042018:505c91d5aad77f4a91440241588970d1",
            "__rnd": 1632579439831
        }


    def getPageJson(self):
        """
        获取单个页面的json数据
        :param self:
        :param page:传入的page参数
        :return:返回页面响应的json数据
        """
        response = requests.post(url=self.url, headers=self.headers, params =self.param ).text
        print(response)
        json_data = json.loads(response,strict=False)
        # 重构from_data
        param_pic_next=json_data["data"]["pic_next"]
        self.param =param_pic_next
        return json_data

    def parserJson(self,json_data):
        """
        解析json数据得到目标数据
        :param json:传入的json数据
        :return:返回目标数据
        """
        # print(json_data)
        results=[]
        pic_lists=json_data["data"]["pic_list"]
        # print(pic_lists)
        for pic_list in pic_lists:
            pic=pic_list["clear_picSrc"][2:].replace("mw1024","large")
            results.append(pic)
        return results

    def imgDownload(self,results):
        for picSrc in results:
            print(picSrc.split("/"))
            img_name = picSrc.split("/")[-1]

            img_data = requests.get(url="https://" + picSrc, headers=self.headers)
            with open(img_name, "wb") as f:
                f.write(img_data.content)
                print("已下载完成:{}".format(img_name))

    def startCrawler(self):
        # try:
        #     while True:
        #         page_json=self.getPageJson()
        #         results = self.parserJson(page_json)
        #         self.imgDownload(results)
        # except:
        #     print("任务失败")
        page_json = self.getPageJson()
        results = self.parserJson(page_json)
        self.imgDownload(results)



if __name__ == '__main__':
    weibo = Weibo()
    weibo.headers["cookie"]=input("请输入您的cookie:")
    weibo.startCrawler()
