import json
import re
from lxml import etree

class HandleResponse:
    def __init__(self):
        self.res_rows = {}

    def get_maintoken(self,response):
        selector = etree.HTML(response.text)
        requesttoken = selector.xpath('//div[@id="page-container"]/input[@name="__RequestVerificationToken"]/@value')[0]
        return  str(requesttoken)

    def get_accurl(self,response):
        try:
            rows = self.res_rows = json.loads(response.text)['Rows'][0]
            url = 'accountId=' + (rows['AccountId'] if (rows['AccountId'] != None) else '')+ '&'
            url = url + 'externalaccountid=' + rows['ExternalAccountId'] + '&'
            url = url + 'currentAccountId=' + (rows['AccountId'] if (rows['AccountId'] != None) else '') + '&'
            url = url + 'identityType=OCPTenantID&identityValue=' + rows['ExternalAccountId']
        except:
            print(response.text)
        else:
            return url

    def get_suburl(self):
        try:
            rows = self.res_rows
            url = 'itemId=undefined&identityType=OCPTenantID&identityValue=' + rows['ExternalAccountId'] + '&'
            url = url + 'currentAccountId=' + (rows['AccountId'] if (rows['AccountId'] != None)  else '')+ '&'
            url = url + 'currentExternalAccountId=' + rows['ExternalAccountId'] + '&'
            url = url + '__RequestVerificationToken='
        except:
            print(self.res_rows)
        else:
            return url

    def get_partnername(self, response):
        pncoll = []
        if response:
            pname = re.finditer('[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+\（?[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+\）?[\u4e00-\u9fa5_a-zA-Z0-9_\.?,?\s]+ [0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}',response.text[1:25000], re.M|re.I)
            if pname:
                for match in pname:
                    pncoll.append(match.group(0))
            if not pname:
                pncoll.append(None)
        else:
            pncoll.append('TenantId不存在')

        return pncoll

