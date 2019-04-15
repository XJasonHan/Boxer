from DBOperator import *
from concurrent.futures import as_completed, ThreadPoolExecutor, ProcessPoolExecutor
from Pages import *
import threading
import time
import copy
lock=threading.Lock()

class implementation:
    # def __init__(self):
    def create_accpage(self,cspage,tenant):
        accountPage = None
        if type(tenant) == str:
            tid = tenant
        else:
            tid = tenant.tenantid

        acc_req_url=cspage.get_account_url(tid)

        if acc_req_url != None:
            accountPage=AccountPage(acc_req_url)

        return accountPage

    def iterate_offer(self,accountpage,partners,tenant):
        dbop=DBOperator()
        offers=[]
        for partner in partners:
            # partnerid=partner.split(' ')[1]
            # partnername=partner.split(' ')[0]
            tpinfo=dbop.get_tpinfo(tenant.tenantid,  partner.split(' ')[0])
            if tpinfo is None:
                print('\033[0;37;41mCannot search in DB with tenant id: %s and partner: %s\033[0m' % (tenant.tenantid, partner.split(' ')[0]))
                continue
            offer=accountpage.get_offers_by_partner(partner.split(' ')[1], tpinfo.id)
            offers.extend(offer)

        return offers

    def impl_get_partners(self,cspage, tenant):
        try:
            accountpage= self.create_accpage(cspage,tenant)
            partnernamecoll=[]
            if accountpage != None:
                partners = accountpage.get_partners()
                if partners:
                    print('%s:%s' % (tenant, partners))
                    if not all:
                        partnernamecoll.append(partners[0][0:-37])
                    else:
                        for pname in partners:
                            partnernamecoll.append(pname[0:-37])
                else:
                    partnernamecoll.append('不是CSP客户')
                    print('%s:%s' % (tenant, '不是CSP客户'))
            else:
                partnernamecoll=[]
                partnernamecoll.append('TenantID 不存在')
                print('%s:%s' % (tenant, '不是CSP客户'))
        except IndexError:
            partnernamecoll=[]
            partnernamecoll.append('不是CSP客户')
            print('%s:%s' % (tenant, '不是CSP客户'))
        else:
            return partnernamecoll

    def impl_get_offers(self,cspage,tenant):
        accountpage=self.create_accpage(cspage,tenant)
        partners=accountpage.get_partners()
        offers=self.iterate_offer(accountpage,partners,tenant)

        return offers

class program:
    def __init__(self):
        self.tg=DBOperator()
        self.customersearchpage=CustomerSearchPage()
        # self.lock=threading.Lock()

    def get_partners(self,tenant):
        try:
            impl = implementation()
            partners = impl.impl_get_partners(copy.deepcopy(self.customersearchpage),tenant)
            return partners
        except:
            print('Tenant id is: '+ tenant)

    def get_offers(self, tenant):
        try:
            impl=implementation()
            #lock.acquire()
            offers=impl.impl_get_offers(copy.deepcopy(self.customersearchpage),tenant)
            #lock.release()

            return offers
        except TypeError:
            print('Tenant id is: '+ tenant.tenantid)
            raise

    def divide_to_perform(self, arr, get_func,fill_in):
        group=int(len(arr) / 100)
        mod=len(arr) % 100
        for i in range(1, group + 1):
            dict=self.parall_exec(arr[(i - 1) * 100:i * 100-1], get_func)
            fill_in(dict)

        dict=self.parall_exec(arr[-mod:], get_func)
        fill_in(dict)

    def seq_to_perform(self, tenants, func):
        for tenant in tenants:
            func(tenant)

    def parall_exec(self,tenants, func):
        dict={}
        with ThreadPoolExecutor(max_workers=8) as executor:
            futs={executor.submit(func, i): i for i in tenants}
        for fut in as_completed(futs):
            dict[futs[fut]]=fut.result()
        return dict

    def main(self):
        p=time.time()
        self.tg.Update_cct()
        partial_tenants=self.tg.get_tenantIds_not_in_cct()
        #all_tenants=self.tg.get_all_tenants()[0:50]

        self.divide_to_perform(partial_tenants,self.get_partners,self.tg.fill_partner_in_tpmt)
        self.tg.Update_cct()
        #self.divide_to_perform(all_tenants, self.get_offers, self.tg.fill_offerdetail)
        #self.seq_to_perform(all_tenants,self.get_offers)

        self.tg.update_case_type()
        n=time.time()
        print("Elapsed : %s" %(n-p))

if __name__ == '__main__':
    p=program()
    p.main()
