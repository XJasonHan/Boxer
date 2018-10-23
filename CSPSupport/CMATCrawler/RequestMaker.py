import requests
import json
from Constant import *
from HandleCookies import HandleCookies
from HandleResponse import HandleResponse
import threading


class RequestMaker:

    def __init__(self):
        self.hres=HandleResponse()
        self.search_token=''
        self.lock=threading.Lock()

    def mainpage_request(self):
        res=requests.get(search_page, cookies=HandleCookies.dict())
        return res

    def search_request(self, tenantId):
        res=self.mainpage_request()
        self.search_token=self.hres.get_maintoken(res)
        search_pay_load['__RequestVerificationToken']=self.search_token
        search_pay_load['tenantGuid']=tenantId
        search_header['cookie']=HandleCookies.get_raw()
        res=requests.post(search_url, data=search_pay_load, headers=search_header)
        return res

    def sub_request(self, tenantId):
        search_res=self.search_request(tenantId)
        if search_res.text.find('doesn') > 0 or search_res.text.find('TenantId is empty') > 0:
            print('TenantId %s does not exist' % tenantId)
            res=None
        else:
            acc_url=account_page + self.hres.get_accurl(search_res)
            acc_token=self.hres.get_maintoken(requests.get(acc_url, cookies=HandleCookies.dict()))
            url=self.hres.get_suburl()
            url=sub_url + url + acc_token
            res=requests.get(url, cookies=HandleCookies.dict())
        return res
