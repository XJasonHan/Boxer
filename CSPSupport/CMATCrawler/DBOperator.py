from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from model import *
import re
import pyodbc

#COON_STR='mssql+pyodbc://********:!******@********.database.chinacloudapi.cn/PartnerCaseReport?driver=SQL+Server+Native+Client+11.0'
#COON_STR='mssql+pyodbc://*******:*******@localhost/CSPCopy?driver=SQL+Server+Native+Client+11.0'
COON_STR='mssql+pyodbc://*******:*******@********.database.chinacloudapi.cn/CorpBI?driver=SQL+Server+Native+Client+11.0'
engine=create_engine(COON_STR, max_overflow=5, echo=True)


class DBOperator:
    def get_all_tenants(self):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        allinfo=session.query(TenantsPartnersMappingTable.tenantid)\
            .filter(TenantsPartnersMappingTable.parntner != None, TenantsPartnersMappingTable.parntner!='', TenantsPartnersMappingTable.crawl_status==0).distinct().all()
        session.close()
        return allinfo

    def get_tpinfo(self,tenantid, partnername):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        tpinfo=session.query(TenantsPartnersMappingTable.id).filter(TenantsPartnersMappingTable.tenantid==tenantid,
                                                                 TenantsPartnersMappingTable.parntner==partnername,
                                                                    TenantsPartnersMappingTable.crawl_status==0).first()
        session.close()
        return tpinfo

    def get_tenantIds_not_in_cct(self):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        tenantids=session.query(t_CustomerCaseTable.columns['TenantID']).filter(t_CustomerCaseTable.columns['PartnerName'] == None).distinct().all()
        tenantids=[str(result.TenantID).strip() for result in tenantids]
        session.close()
        return tenantids

    def fill_partner_in_cct(self, dict):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        for k in dict.keys():
            for pname in dict[k]:
                session.query(t_CustomerCaseTable.columns['TenantID'], t_CustomerCaseTable.columns['PartnerName']) \
                    .filter(t_CustomerCaseTable.columns['TenantID'] == k) \
                    .update({t_CustomerCaseTable.columns['PartnerName']: pname}, synchronize_session=False)
        session.commit()
        session.close()

    def fill_partner_in_tpmt(self, dict):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        tp_list=[]
        for k in dict.keys():
            if dict[k] is None:
                continue
            else:
                for pname in dict[k]:
                    tpm=TenantsPartnersMappingTable()
                    tpm.tenantid=k
                    tpm.parntner=pname
                    tp_list.append(tpm)
        session.add_all(tp_list)
        session.commit()
        session.close()

    def fill_offerdetail(self,offers):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        offer_list=[]
        for k in offers.keys():
            offer_list.extend(offers[k])
        session.add_all(offer_list)

        dis_tpinfo = list(set([offer.tpinfo for offer in offer_list]))
        for tpinfo in dis_tpinfo:
            session.query(TenantsPartnersMappingTable.crawl_status).filter(TenantsPartnersMappingTable.id==tpinfo).\
            update({TenantsPartnersMappingTable.crawl_status:1},synchronize_session=False)
        session.commit()
        session.close()

    def update_case_type(self):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        arr_dnames=[]
        query_customer=session.query(t_CustomerCaseTable.columns['SR'], t_CustomerCaseTable.columns['OrgID'],
                                     t_CustomerCaseTable.columns['CaseType'])
        query_pdomain=session.query(PartnerTable.DomainName).all()
        for dn in query_pdomain:
            arr_dnames.append(dn[0])

        for row in query_customer.filter(t_CustomerCaseTable.columns['CaseType'] == None,t_CustomerCaseTable.columns['PartnerName']!=None).all():
            if row[1] != None:
                have_set = False
                for dname in arr_dnames:
                    if row[1].find('vip.sina') < 0:
                        if re.search(dname, row[1], re.M | re.I):
                            query_customer.filter(t_CustomerCaseTable.columns['SR'] == row[0]) \
                                .update({t_CustomerCaseTable.columns['CaseType']: 'Partner Case'},
                                        synchronize_session=False)
                            have_set = True
                            break

                if not have_set:
                    query_customer.filter(t_CustomerCaseTable.columns['SR'] == row[0]) \
                        .update({t_CustomerCaseTable.columns['CaseType']: 'EndCustomer Case'},
                           synchronize_session=False)

            else:
                query_customer.filter(t_CustomerCaseTable.columns['SR'] == row[0]).update(
                    {t_CustomerCaseTable.columns['CaseType']: 'EndCustomer Case'},
                    synchronize_session=False)

        session.commit()
        session.close()

    def Update_cct(self):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        conn=engine.connect()

        #Update ParnterName in CustomerCaseTable with exist PartnerName in TenantsPartnersMappingTable
        update_cct=t_CustomerCaseTable.update().values(
            PartnerName=select([TenantsPartnersMappingTable.parntner])\
            .where(TenantsPartnersMappingTable.tenantid==t_CustomerCaseTable.columns['TenantID']).limit(1)
        ).where(t_CustomerCaseTable.columns['PartnerName']==None)
        conn.execute(update_cct)

        #update crawl status for offer detail
        crawl_status=session.query(TenantsPartnersMappingTable.crawl_status).\
            filter(TenantsPartnersMappingTable.parntner != None, TenantsPartnersMappingTable.parntner!='').\
            distinct().all()
        if len(crawl_status)==1:
            session.query(TenantsPartnersMappingTable).update({TenantsPartnersMappingTable.crawl_status:0},synchronize_session=False)

#
        session.close()
