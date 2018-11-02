from RequestMaker import *
from HandleResponse import *
from DBOperator import *
from concurrent.futures import as_completed, ThreadPoolExecutor
import queue
import threading


class Program():
    def __init__(self):
        self.tg=DBOperator()
        self.lock=threading.Lock()

    def get_pnames(self, tenantId, all=False):
        rem=RequestMaker()
        resh=HandleResponse()
        partnernames=resh.get_partnername(rem.sub_request(tenantId))
        partnernamecoll=[]
        if partnernames:
            print('%s:%s' % (tenantId, partnernames))
            if not all:
                partnernamecoll.append(partnernames[0][0:-37])
            else:
                for pname in partnernames:
                    partnernamecoll.append(pname[0:-37])

        else:
            partnernamecoll.append('不是CSP客户')
            print('%s:%s' % (tenantId, '不是CSP客户'))

        return partnernamecoll

    def Main(self, pname_exists, tablename):
        tenantIds=self.tg.get_tenantIds(pname_exists)

        if tablename == 'CustomerCaseTable':
            group=int(len(tenantIds) / 100)
            mod=len(tenantIds) % 100
            for i in range(1, group + 1):
                dict=self.parall_exec(tenantIds[(i - 1) * 100:i * 100], False)
                self.tg.fill_partner_in_cct(dict)

            dict=self.parall_exec(tenantIds[-mod:], False)
            self.tg.fill_partner_in_cct(dict)

        if tablename == 'TenantsPartnersMappingTable':
            group=int(len(tenantIds) / 100)
            mod=len(tenantIds) % 100
            for i in range(1, group + 1):
                dict=self.parall_exec(tenantIds[(i - 1) * 100:i * 100], True)
                self.tg.fill_partner_in_tpmt(dict)

            dict=self.parall_exec(tenantIds[-mod:], True)
            self.tg.fill_partner_in_tpmt(dict)

        if tablename == 'update':
            self.tg.update_case_type()

    def parall_exec(self, tenantIds, getall):
        dict={}
        with ThreadPoolExecutor(max_workers=10) as executor:
            futs={executor.submit(self.get_pnames, i, getall): i for i in tenantIds}
        for fut in as_completed(futs):
            dict[futs[fut]]=fut.result()
        return dict


if __name__ == '__main__':
    p=Program()
    p.Main(True, 'CustomerCaseTable')
    p.Main(False, 'TenantsPartnersMappingTable')
    p.Main(False, 'update')
