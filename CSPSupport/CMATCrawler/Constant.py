search_page='https://cmat.cp.partner.microsoftonline.cn/Customer/CustomerSearch'
account_page='https://cmat.cp.partner.microsoftonline.cn/Customer/Home?'
search_url='https://cmat.cp.partner.microsoftonline.cn/Customer/Search'
sub_url='https://cmat.cp.partner.microsoftonline.cn/Subscription/AllSubscriptions?'
search_header={
    'Host': 'cmat.cp.partner.microsoftonline.cn',
    'Connection': 'keep-alive',
    'Content-Length': '331',
    'Origin': 'https://cmat.cp.partner.microsoftonline.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    #'MS-CV': 'uNo93HANYKXs9bxy.0',
    'Referer': 'https://cmat.cp.partner.microsoftonline.cn/Customer/CustomerSearch',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

search_pay_load = {
    'itemId': 'undefined',
    '__RequestVerificationToken': '',
    'searchType': 'SearchByTenantGuid',
    'tenantGuid': '',
    'PageSize': 10,
    'PageIndex': 0
}

sub_pay_load = {
    'itemId': 'undefined',
    'identityType': 'OCPTenantID',
    'identityValue': '',
    'currentAccountId': '',
    'currentExternalAccountId': '',
    '__RequestVerificationToken': '',
}

