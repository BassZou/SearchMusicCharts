# coding=utf-8

import requests
import urllib.request
import datetime
import json
import sys

class FeiShuBot():
    """
    飞书机器人
    """
    def send_msg(self,title,text):
        """
        goodsongs - 产品 飞书群
        """
        # 产品群
        WEB_HOOK_URL = r'https://open.feishu.cn/open-apis/bot/v2/hook/de4e7d58-4a59-42fc-bc25-4b59e1f137d4'

        headers={"Content-Type": "application/json"}
        data={
                "msg_type": "post",
                "content": {
                    "post": {
                        "zh_cn": {
                            "title": title,
                            "content": [
                                [
                                    {
                                        "tag": "text",
                                        "text": text
                                    }
                                ]
                            ]
                        }
                    }
                }
            } 
        res=requests.post(url=WEB_HOOK_URL,headers=headers,json=data)
        res = json.loads(res.text)
        print('send_msg---',res)
        if res.get('StatusCode') == 0:
            print('send_msg---ok---',res.get('StatusCode'),res.get('StatusMessage'))
        else:
            print('send_msg---no---',res.get('StatusCode'),res.get('StatusMessage'))


    '''
    飞书config----小南自建的飞书
    '''
    __APP_ID = "cli_9fe3d46c7fee900e"
    __APP_SECRET = "f9SIWumKFmRIKkHK8g3g2ejk12DuHDFu"
    __APP_VERIFICATION_TOKEN = "PuZxIXsuW9ZHIae57DHkjgrxnwLlusDr"

    __user_id = '59f921g3' # Bkswag - 小南飞书用户id

    __boturl = r"https://open.feishu.cn/open-apis/message/v4/send/"

    def send_md_feishu(self, title,ceontent):
        token = self.get_tenant_access_token()
        headers={
            "Content-Type": "text/plain",
            "Authorization":  "Bearer "+token
            }

        content = {
                "title": title,
                "content": [
                    [
                        {
                            "tag": "text",
                            "un_escape": True,
                            "text": ceontent
                        },
                        # {
                        #     "tag": "a",
                        #     "text": "超链接",
                        #     "href": "http://www.feishu.cn"
                        # },
                        # {
                        #     "tag": "at",
                        #     "user_id": "ou_18eac85d35a26f989317ad4f02e8bbbb"
                        # }
                    ]
                ]
        }

        data={
            "open_id": "",
            "user_id": self.__user_id,
            "email": "",
            "chat_id": "",
            "msg_type": "post",
            "content":{
                "post":{ 
                    "zh_cn": content
                }
            }
        }
        res=requests.post(url=self.__boturl,headers=headers,json=data)
        print(res.text)


    def get_tenant_access_token(self):
        '''
        获取 Authorization
        tenant_access_token（企业自建应用）
        '''
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
        headers={"Content-Type": "application/json"}
        data={
                "app_id": self.__APP_ID,
                "app_secret": self.__APP_SECRET
            }
        res=requests.post(url=url,headers=headers,json=data)
        res = json.loads(res.text)
        if res.get('code') == 0:
            print('get_tenant_access_token---',res.get('tenant_access_token'))
            return res.get('tenant_access_token')
        else:
            print('---->get_tenant_access_token 失败', res)
            return None


    









