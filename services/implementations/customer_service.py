from repos.implementations.customer_repo import Customer_Repo
from services.interfaces.customer_interface import Customer_Service_Interface


class Customer_Service(Customer_Service_Interface):

    def __init__(self):
        self.customer_repo = Customer_Repo()

    def get_all_customers(self):
        return self.customer_repo.get_all_customers()

    def slowTest(self):
        return self.someAPICall() + 1

    def someAPICall(self):
        return 0

