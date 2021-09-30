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
        self.uid=0
        self.page=0
        self.since_id=""
        self.url = "https://weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0&since_id={}".format(self.uid,self.page,self.since_id)
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "referer": "https://weibo.com/u/{}?tabtype=feed".format(self.uid),
            # 需要更改自己cookie
            "Cookie":""
        }




    def getPageJson(self):
        """
        获取单个页面的json数据
        :param self:
        :param page:传入的page参数
        :return:返回页面响应的json数据
        """
        self.page += 1
        self.url = "https://weibo.com/ajax/statuses/mymblog?uid={}&page={}".format(self.uid, self.page)
        print(self.url)
        response = requests.get(url=self.url, headers=self.headers).text
        json_data = json.loads(response, strict=False)

        return json_data

    def parserJson(self,json_data):
        """
        解析json数据得到目标数据
        :param json:传入的json数据
        :return:返回目标数据
        """
        # print(json_data)
        results=[]
        self.since_id=json_data["data"]["since_id"]


        lists = json_data["data"]["list"]

        for x in lists:

            try:
                for pic_ids_list in x["pic_ids"]:
                    pic=x["pic_infos"][pic_ids_list]["thumbnail"]["url"].replace("wap180", "large")
                    results.append(pic)
            except:

                print(x["page_info"])
        # print(results)
        return results
    def parserJson_video(self, json_data):
        """
        解析json数据得到目标数据
        :param json:传入的json数据
        :return:返回目标视频数据
        """
        # print(json_data)
        results = []

        lists = json_data["data"]["list"]
        stream_url_hd = []
        name = []
        for x in lists:
            if "page_info" in x:
                try:
                    # print("####3333",x["page_info"]["media_info"]["stream_url_hd"])
                    name.append(x["page_info"]["media_info"]["name"]+".mp4")
                    stream_url_hd.append(x["page_info"]["media_info"]["stream_url_hd"])
                except:
                    print("")
        zip_data = zip(stream_url_hd, name)
        return zip_data


    def imgDownload(self,results):
        for picSrc in results:
            # print(picSrc.split("/"))
            img_name = picSrc.split("/")[-1]

            img_data = requests.get(url= picSrc, headers=self.headers)
            with open(img_name, "wb") as f:
                f.write(img_data.content)
                print("已下载完成:{}".format(img_name))

    def videoDownload(self, zip_data):
        try:
            for stream_url_hd, video_name in zip_data:
                img_data = requests.get(url=stream_url_hd, headers=self.headers)
                with open(video_name, "wb") as f:
                    f.write(img_data.content)
                    print("已下载完成:{}".format(video_name))
        except:
            pass
    def startCrawler(self):
        try:
            while True:
                page_json = self.getPageJson()
                video_results = self.parserJson_video(page_json)
                results = self.parserJson(page_json)
                self.imgDownload(results)
                self.videoDownload(video_results)
        except:
            print("任务失败")


if __name__ == '__main__':
    weibo = Weibo()
    weibo.headers["cookie"]=input("请输入您的cookie:")
    weibo.uid=input("请输入微博uid：\n")
    weibo.startCrawler()
