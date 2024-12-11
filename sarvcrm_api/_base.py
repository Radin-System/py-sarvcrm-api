from .modules import *

class ApiRouteMixin:
    def __init__(self) -> None:
        self.Accounts = Accounts(self)
        self.AosContracts = AosContracts(self)
        self.AosInvoices = AosInvoices(self)
        self.AosPdfTemplates = AosPdfTemplates(self)
        self.AosProductCategories = AosProductCategories(self)
        self.AosProducts = AosProducts(self)
        self.AosQuotes = AosQuotes(self)
        self.Appointments = Appointments(self)
        self.Approval = Approval(self)
        self.AsolProject = AsolProject(self)
        self.Branches = Branches(self)
        self.Bugs = Bugs(self)
        self.Calls = Calls(self)
        self.Cases = Cases(self)
        self.Communications = Communications(self)
        self.CommunicationsTarget = CommunicationsTarget(self)
        self.CommunicationsTemplate = CommunicationsTemplate(self)
        self.Campaigns = Campaigns(self)
        self.Contacts = Contacts(self)
        self.Deposits = Deposits(self)
        self.Documents = Documents(self)
        self.Emails = Emails(self)
        self.KnowledgeBase = KnowledgeBase(self)
        self.KnowledgeBaseCategories = KnowledgeBaseCategories(self)
        self.Leads = Leads(self)
        self.Meetings = Meetings(self)
        self.Notes = Notes(self)
        self.ObjConditions = ObjConditions(self)
        self.ObjIndicators = ObjIndicators(self)
        self.ObjObjectives = ObjObjectives(self)
        self.Opportunities = Opportunities(self)
        self.Payments = Payments(self)
        self.PurchaseOrder = PurchaseOrder(self)
        self.ScCompetitor = ScCompetitor(self)
        self.ScContract = ScContract(self)
        self.ScContractManagement = ScContractManagement(self)
        self.ServiceCenters = ServiceCenters(self)
        self.Tasks = Tasks(self)
        self.Timesheet = Timesheet(self)
        self.Vendors = Vendors(self)