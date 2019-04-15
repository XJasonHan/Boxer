from Constant import *
from HandleCookies import HandleCookies
import requests
import json
import re
import datetime
from model import *
from lxml import etree


class AbstractPage:
    def __init__(self, base_url):
        self.base_url=base_url
        self.cons=Constant()

    def get_token(self, res):
        selector=etree.HTML(res.text)
        requesttoken=selector.xpath('//div[@id="page-container"]/input[@name="__RequestVerificationToken"]/@value')[0]
        return str(requesttoken)


class CustomerSearchPage(AbstractPage):
    def __init__(self, url=search_base_url):
        AbstractPage.__init__(self, url)
        res=requests.get(self.base_url, cookies=HandleCookies.dict())
        self.token=self.get_token(res)
        self.cons.search_header['cookie']=HandleCookies.get_raw()
        self.cons.search_pay_load['__RequestVerificationToken']=self.token

    def get_account_url(self, tenantid):
        self.cons.search_pay_load['tenantGuid']=tenantid

        res=requests.post(search_req_url, data=self.cons.search_pay_load, headers=self.cons.search_header)

        if res.text.find('doesn') > 0 or res.text.find('TenantId is empty') > 0:
            #print('TenantId %s does not exist' % tenantid)
            acc_url = None
        else:
            self.res_rows=json.loads(res.text)['Rows'][0]
            acc_url=self.__get_accurl

        return acc_url

    @property
    def __get_accurl(self):
        try:
            url='accountId=' + (self.res_rows['AccountId'] if (self.res_rows['AccountId'] != None) else '') + '&'
            url=url + 'externalaccountid=' + self.res_rows['ExternalAccountId'] + '&'
            url=url + 'currentAccountId=' + (self.res_rows['AccountId'] if (self.res_rows['AccountId'] != None) else '') + '&'
            url=url + 'identityType=OCPTenantID&identityValue=' + self.res_rows['ExternalAccountId'] + '&'
            url=url + 'identityEmail=N%2FA'
        except:
            print(self.res_rows)
        else:
            return url

    @property
    def AccountId(self):
        return self.res_rows['AccountId']

    @property
    def ExternalAccountId(self):
        return self.res_rows['ExternalAccountId']


class CustomerOVPage(AbstractPage):
    def __init__(self, url=account_overview_url, token=None, accountid = None, tenantid = None):
        AbstractPage.__init__(self, url)

    def __get_overview_url(self, tenantid, accountid, token):
        url = account_overview_url + tenantid + "&currentAccountId="
        url = url + accountid + '&currentExternalAccountId='
        url = url + tenantid + '&__RequestVerificationToken=' + token
        return url

class AccountPage(AbstractPage):
    def __init__(self, req_url, url=account_base_url):
        AbstractPage.__init__(self, url)
        self.req_url=req_url
        self.tenantid=self.params['externalaccountid']
        self.accountid=self.params['accountId']

        res=requests.get(self.base_url + self.req_url, cookies=HandleCookies.dict())
        self.token=self.get_token(res)

        additional_cookie=res.cookies.keys()[0] + '=' + res.cookies[res.cookies.keys()[0]]
        #url_overview=self.__get_overview_url(self.tenantid,self.accountid,self.token)
        #startdate=self.get_startdate(url_overview,HandleCookies.dict())

        self.cookies=HandleCookies.update_accpagecookies(additional_cookie,self.tenantid)

    def get_partners(self):
        url=self.__get_suburl(self.tenantid, self.accountid)
        url=allsub_url + url + self.token
        res=requests.get(url, cookies=HandleCookies.dict())
        resellers=[]
        if res:
            pname=re.finditer(
                '[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+\（?[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+\）?[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+ [0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}',
                res.text[1:30000],
                re.M | re.I)
            if pname:
                for match in pname:
                    resellers.append(match.group(0))
            if not pname:
                resellers.append(None)
        else:
            resellers.append('TenantId不存在')

        return resellers

    def get_offers_by_partner(self, partnerid, tpinfo):
        self.cons.offerdetail_req_header['__RequestVerificationToken']=HandleCookies.dict()[' __RequestVerificationToken']
        self.cons.offerdetail_pay_load['currentAccountId']=self.accountid
        self.cons.offerdetail_pay_load['currentExternalAccountId']=self.tenantid
        self.cons.offerdetail_pay_load['identityValue']=self.tenantid
        self.cons.offerdetail_pay_load['ResellerPartnerCAID']=partnerid
        self.cons.offerdetail_pay_load['__RequestVerificationToken']=self.token
        self.cons.offerdetail_req_header['referer']=account_base_url + self.req_url
        self.cons.offerdetail_req_header['cookie']=self.cookies
        res=requests.post(offerdetail_req_url, data=self.cons.offerdetail_pay_load, headers=self.cons.offerdetail_req_header)
        offers=self.__get_offers(res, tpinfo)
        return offers

    def __get_overview_url(self, tenantid, accountid, token):
        url = account_overview_url + tenantid + "&currentAccountId="
        url = url + accountid + '&currentExternalAccountId='
        url = url + tenantid + '&__RequestVerificationToken=' + token
        return url

    def __get_suburl(self, tenantid, accountid):
        url='itemId=undefined&identityType=OCPTenantID&identityValue=' + tenantid + '&'
        url=url + 'currentAccountId=' + accountid + '&'
        url=url + 'currentExternalAccountId=' + tenantid + '&'
        url=url + '__RequestVerificationToken='
        return url

    def __get_offers(self, response, tenantpartner_no):
        offers=[]
        if response.text.find('Rows') > 0:
            rows=json.loads(response.text)['Rows']
            if len(rows) > 0:
                for row in rows:
                    offerrow=Offerdetailtable()
                    offerrow.tpinfo=tenantpartner_no
                    offerrow.offer_name=row['Name']
                    offerrow.purchase_date=datetime.datetime.strptime(row['PurchaseDate'], '%m/%d/%Y')
                    offerrow.start_date=datetime.datetime.strptime(row['StartDate'], '%m/%d/%Y')
                    offerrow.end_date=datetime.datetime.strptime(row['EndDate'], '%m/%d/%Y')
                    offerrow.seat_count=row['InstanceCount']
                    offerrow.billed_cycle=row['BilledCycle']
                    offerrow.status=row['StatusString']
                    offers.append(offerrow)
            else:
                offerrow=Offerdetailtable()
                offerrow.tpinfo=tenantpartner_no
                offerrow.offer_name=None
                offerrow.purchase_date=None
                offerrow.start_date=None
                offerrow.end_date=None
                offerrow.seat_count=None
                offerrow.billed_cycle=None
                offerrow.status=None
                offers.append(offerrow)
        else:
            print(response.text)

        return offers

    @property
    def params(self):
        list_by_symbol=self.req_url.split('&')
        result={}
        for str in list_by_symbol:
            if str.find('accountId') > -1:
                result['accountId']=str.split('=')[1]
            if str.find('externalaccountid') > -1:
                result['externalaccountid']=str.split('=')[1]

        return result

    def get_startdate(self,url,cookies):
        res = requests.get(url,cookies=cookies)
        overview_data = re.search('var accountInfoDetailData =.*',res.text)[0].strip()
        json_data=overview_data.split('=')[1]
        json_data=json.loads(json_data[0:len(json_data)-1])
        f_result=list(filter(lambda x:x['Name']=='startdate',json_data['Tags']))
        try:
            startdate=f_result[0]['Value']
            return startdate
        except IndexError:
            print('The Tenant is %s' % (self.tenantid))
            raise IndexError


