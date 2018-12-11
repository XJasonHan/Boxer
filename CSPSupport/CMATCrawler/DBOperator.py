from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *
import re
import pyodbc

COON_STR='mssql+pyodbc://pbiadmin:!QAZ2wsx1234@pbireporting.database.chinacloudapi.cn/PartnerCaseReport?driver=SQL+Server+Native+Client+11.0'
engine=create_engine(COON_STR, max_overflow=5, echo=True)


class DBOperator:
    def get_tenantIds(self, pname_exists=True):
        smaker=sessionmaker(bind=engine)
        session=smaker()
        if pname_exists:
            tenantids=session.query(t_CustomerCaseTable.columns['TenantID']).filter(t_CustomerCaseTable.columns['PartnerName'] == None).distinct().all()
        else:
            tenantids=session.query(t_CustomerCaseTable.columns['TenantID'])\
                .outerjoin(TenantsPartnersMappingTable, TenantsPartnersMappingTable.tenantid == t_CustomerCaseTable.columns['TenantID'])\
                .filter(TenantsPartnersMappingTable.tenantid == None)\
                .distinct().all()
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
            for pname in dict[k]:
                tprow=TenantsPartnersMappingTable()
                tprow.tenantid=k
                tprow.parntner=pname
                tp_list.append(tprow)

        session.add_all(tp_list)
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

        for row in query_customer.filter(t_CustomerCaseTable.columns['CaseType'] == None).all():
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
