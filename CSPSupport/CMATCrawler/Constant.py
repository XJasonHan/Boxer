search_base_url='https://cmat.cp.partner.microsoftonline.cn/Customer/CustomerSearch'
account_base_url='https://cmat.cp.partner.microsoftonline.cn/Customer/Home?'
search_req_url='https://cmat.cp.partner.microsoftonline.cn/Customer/Search'
allsub_url='https://cmat.cp.partner.microsoftonline.cn/Subscription/AllSubscriptions?'
offerdetail_req_url='https://cmat.cp.partner.microsoftonline.cn/Subscription/_GetSubscriptions'
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
account_overview_url='https://cmat.cp.partner.microsoftonline.cn/Customer/OverView?itemId=undefined&identityType=OCPTenantID&identityValue='

class Constant:
    def __init__(self):
        self.search_header={
            'Host': 'cmat.cp.partner.microsoftonline.cn',
            'Connection': 'keep-alive',
            'Content-Length': '331',
            'Origin': 'https://cmat.cp.partner.microsoftonline.cn',
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            #'MS-CV': 'uNo93HANYKXs9bxy.0',
            'Referer': 'https://cmat.cp.partner.microsoftonline.cn/Customer/CustomerSearch',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        self.offerdetail_req_header = {
            # 'authority': 'https://cmat.cp.partner.microsoftonline.cn',
            # 'method': 'POST',
            # 'path': '/Subscription/_GetSubscriptions',
            # 'scheme': 'https',
            'accept':'*/*',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
            'Connection':'keep-alive',
            'content-length':'590',
            'content-type':'application/x-www-form-urlencoded',
            'ms-cv': '',
            'DNT':'1',
            'origin':'https://cmat.cp.partner.microsoftonline.cn',
            'referer':'',
            'user-agent':user_agent,
            'x-requested-with': 'XMLHttpRequest',
            'host':'cmat.cp.partner.microsoftonline.cn'

        }

        self.search_pay_load = {
            'itemId': 'undefined',
            '__RequestVerificationToken': '',
            'searchType': 'SearchByTenantGuid',
            'tenantGuid': '',
            'PageSize': 10,
            'PageIndex': 0
        }

        self.sub_pay_load = {
            'itemId': 'undefined',
            'identityType': 'OCPTenantID',
            'identityValue': '',
            'currentAccountId': '',
            'currentExternalAccountId': '',
            '__RequestVerificationToken': '',
        }

        self.offerdetail_pay_load = {
            'itemId': 'undefined',
            'identityType': 'OCPTenantID',
            'identityValue': '',
            'currentAccountId':'',
            'currentExternalAccountId': '',
            '__RequestVerificationToken': '',
            'SubsStatusFilter':'AllStatus',
            'PurchaseChannel': 'Reseller',
            'ResellerPartnerCAID':'',
            'SubsSearchCriteria': 'SubsID',
            'SearchContent':'',
            'Pagerable': False,
            #'TrackingGuid':'',
            'PageSize': 0,
            'PageIndex': 0
        }