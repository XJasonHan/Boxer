import urllib.parse
import re

class HandleCookies:
    @staticmethod
    def dict():
        re_data = {}
        with open('Raw_Cookies', 'r') as file:
            d=file.read()
            split_data=d.split(';')
            for record in split_data:
                record_split=record.split('=')
                re_data[record_split[0]]=record_split[1]

        return re_data

    @staticmethod
    def get_raw():
        with open('Raw_Cookies', 'r') as file:
            raw = file.read()

        return raw

    @staticmethod
    def update_accpagecookies(additional,tenantid):
        repl_format=r'extendDictionary%22%3a%5b%7b%22Key%22%3a%22OMSSubsId%22%2c%22Value%22%3a%2200000000-0000-0000-0000-0000000' \
                         r'00000%22%7d%2c%7b%22Key%22%3a%22PublicCustomerNumber%22%2c%22Value%22%3anull%7d%2c%7b%22Key%22%3a%22Backfi' \
                         r'llStatus%22%2c%22Value%22%3anull%7d%2c%7b%22Key%22%3a%22SearchByTenantGuid%22%2c%22Value%22%3a%22%s%22%7d%' \
                         r'2c%7b%22Key%22%3a%22O365TenantGuid%22%2c%22Value%22%3a%22%s%22%7d%2c%7b%22Key%22%3a%22LocalCurrency%22%2c%' \
                         r'22Value%22%3a%22CNY%22%7d%2c%7b%22Key%22%3a%22Tags%22%2c%22Value%22%3a%22o365.microsoft.com%5c%2fversion%3' \
                         r'd15+o365.microsoft.com%22%7d%5d%7d'
                         #r'd15+o365.microsoft.com%5c%2fstartdate%3d%s%22%7d%5d%7d' \


        pattern='extendDictionary.*'
        original=HandleCookies.get_raw()
        repl=urllib.parse.unquote(repl_format)
        repl=repl%(tenantid,tenantid)
        repl=urllib.parse.quote(repl)
        update=re.sub(pattern, repl, additional)
        after_update=update+';'+original
        return after_update

