# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Integer, NCHAR, String, Table, Unicode, text
from sqlalchemy.dialects.mssql.base import BIT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_CustomerCaseTable = Table(
    'CustomerCaseTable', metadata,
    Column('Title', Unicode(800)),
    Column('SR', Unicode(14), nullable=False),
    Column('Severity', NCHAR(10)),
    Column('Engineer', Unicode(50)),
    Column('Company', Unicode(300)),
    Column('Product', Unicode(50)),
    Column('IssueCode', Unicode(300)),
    Column('InquireType', Unicode(50)),
    Column('Description', Unicode),
    Column('EngageMethod', Unicode(50)),
    Column('SLA', Unicode(50)),
    Column('SLATime', DateTime),
    Column('Status', Unicode(50)),
    Column('CloseReason', Unicode(300)),
    Column('Creator', Unicode(50)),
    Column('ContactPerson', Unicode(300)),
    Column('TenantID', NCHAR(40)),
    Column('closedclassification', Unicode(50)),
    Column('CustomerType', Unicode(50)),
    Column('LookUpSource', Unicode(50)),
    Column('PoDCategory', Unicode(300)),
    Column('PoDProblemType', Unicode(300)),
    Column('PoDProduct', Unicode(300)),
    Column('ReportMonth', Unicode(10)),
    Column('ItemID', CHAR(12, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('PartnerName', Unicode(300)),
    Column('PartnerType', Unicode(300)),
    Column('CaseType', Unicode(300)),
    Column('Seat', Integer),
    Column('OrgID', Unicode(300)),
    Column('SubscriptionID', Unicode(100)),
    Column('Modifier', Unicode(50)),
    Column('CreationTime', DateTime),
    Column('ModificationTime', DateTime),
    Column('AzulPartner', Unicode(300))
)


t_CustomerCaseTableErrorRows = Table(
    'CustomerCaseTableErrorRows', metadata,
    Column('Title', Unicode(800)),
    Column('SR', Unicode, nullable=False),
    Column('Severity', NCHAR(10)),
    Column('Engineer', Unicode),
    Column('Company', Unicode),
    Column('Product', Unicode),
    Column('IssueCode', Unicode),
    Column('InquireType', Unicode),
    Column('Description', Unicode),
    Column('EngageMethod', Unicode),
    Column('SLA', Unicode),
    Column('SLATime', DateTime),
    Column('Status', Unicode),
    Column('CloseReason', Unicode),
    Column('Creator', Unicode),
    Column('ContactPerson', Unicode),
    Column('TenantID', Unicode),
    Column('closedclassification', Unicode),
    Column('CustomerType', Unicode),
    Column('LookUpSource', Unicode),
    Column('PoDCategory', Unicode),
    Column('PoDProblemType', Unicode),
    Column('PoDProduct', Unicode),
    Column('ReportMonth', Unicode),
    Column('ItemID', CHAR(12, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('PartnerName', Unicode),
    Column('PartnerType', Unicode),
    Column('CaseType', Unicode),
    Column('Seat', Integer),
    Column('OrgID', Unicode),
    Column('ErrorCode', Integer),
    Column('ErrorColumn', Integer),
    Column('ErrorDescription', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('SubscriptionID', Unicode),
    Column('Modifier', Unicode),
    Column('CreationTime', DateTime),
    Column('ModificationTime', DateTime),
    Column('AzulPartner', Unicode)
)


t_Dim_CustomerTenant = Table(
    'Dim_CustomerTenant', metadata,
    Column('tenantID', NCHAR(40))
)


t_PartnerDomain = Table(
    'PartnerDomain', metadata,
    Column('ChineseName', Unicode(255)),
    Column('DomainName', Unicode(255)),
    Column('#EnglishName', Integer)
)


class PartnerTable(Base):
    __tablename__ = 'PartnerTable'

    EngilishName = Column(Unicode(255))
    ChineseName = Column(Unicode(255))
    DomainName = Column(Unicode(255))
    id = Column(Integer, primary_key=True)


t_Partners = Table(
    'Partners', metadata,
    Column('ChineseName', Unicode(255)),
    Column('Domains', Integer)
)


t_StagingCustomerCase = Table(
    'StagingCustomerCase', metadata,
    Column('Title', Unicode(800)),
    Column('SR', Unicode(14), nullable=False),
    Column('Severity', NCHAR(10)),
    Column('Engineer', Unicode(50)),
    Column('Company', Unicode(300)),
    Column('Product', Unicode(50)),
    Column('IssueCode', Unicode(300)),
    Column('InquireType', Unicode(50)),
    Column('Description', Unicode),
    Column('EngageMethod', Unicode(255)),
    Column('SLA', Unicode(50)),
    Column('SLATime', DateTime),
    Column('Status', Unicode(255)),
    Column('CloseReason', Unicode(300)),
    Column('Creator', Unicode(50)),
    Column('ContactPerson', Unicode(300)),
    Column('TenantID', NCHAR(40)),
    Column('closedclassification', Unicode(50)),
    Column('CustomerType', Unicode(50)),
    Column('LookUpSource', Unicode(50)),
    Column('PoDCategory', Unicode(300)),
    Column('PoDProblemType', Unicode(300)),
    Column('PoDProduct', Unicode(300)),
    Column('ReportMonth', Unicode(10)),
    Column('ItemID', CHAR(12, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('PartnerName', Unicode(300)),
    Column('PartnerType', Unicode(300)),
    Column('CaseType', Unicode(300)),
    Column('Seat', Integer),
    Column('OrgID', Unicode(300)),
    Column('SubscriptionID', Unicode(100)),
    Column('Modifier', Unicode(50)),
    Column('CreationTime', DateTime),
    Column('ModificationTime', DateTime),
    Column('AzulPartner', Unicode(300))
)


t_StagingCustomerCaseErrorRows = Table(
    'StagingCustomerCaseErrorRows', metadata,
    Column('Title', Unicode(800)),
    Column('SR', Unicode, nullable=False),
    Column('Severity', NCHAR(10)),
    Column('Engineer', Unicode),
    Column('Company', Unicode),
    Column('Product', Unicode),
    Column('IssueCode', Unicode),
    Column('InquireType', Unicode),
    Column('Description', Unicode),
    Column('EngageMethod', Unicode),
    Column('SLA', Unicode),
    Column('SLATime', DateTime),
    Column('Status', Unicode),
    Column('CloseReason', Unicode),
    Column('Creator', Unicode),
    Column('ContactPerson', Unicode),
    Column('TenantID', Unicode),
    Column('closedclassification', Unicode),
    Column('CustomerType', Unicode),
    Column('LookUpSource', Unicode),
    Column('PoDCategory', Unicode),
    Column('PoDProblemType', Unicode),
    Column('PoDProduct', Unicode),
    Column('ReportMonth', Unicode),
    Column('ItemID', CHAR(12, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('PartnerName', Unicode),
    Column('PartnerType', Unicode),
    Column('CaseType', Unicode),
    Column('Seat', Integer),
    Column('OrgID', Unicode),
    Column('ErrorCode', Integer),
    Column('ErrorColumn', Integer),
    Column('ErrorDescription', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('SubscriptionID', Unicode),
    Column('Modifier', Unicode),
    Column('CreationTime', DateTime),
    Column('ModificationTime', DateTime),
    Column('AzulPartner', Unicode)
)


class TenantsPartnersMappingTable(Base):
    __tablename__ = 'TenantsPartnersMappingTable'

    tenantid = Column(Unicode(40))
    parntner = Column(Unicode(50))
    id = Column(Integer, primary_key=True)
    crawl_status = Column(BIT, nullable=False, server_default=text("((0))"))


class Offerdetailtable(Base):
    __tablename__ = 'offerdetailtable'

    id = Column(Integer, primary_key=True)
    tpinfo = Column(ForeignKey('TenantsPartnersMappingTable.id'), nullable=False)
    offer_name = Column(Unicode(60))
    purchase_date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    seat_count = Column(Integer)
    billed_cycle = Column(Unicode(40))
    status = Column(Unicode(40))
    insert_datetime = Column(DateTime, server_default=text("(getdate())"))

    TenantsPartnersMappingTable = relationship('TenantsPartnersMappingTable')
