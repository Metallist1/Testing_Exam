from repos.db.fake_db import get_customer_db
from repos.interfaces.customer_repo_interface import Customer_Repo_Interface


class Customer_Repo(Customer_Repo_Interface):

    def __init__(self):
        self.customer_table = get_customer_db()

    def get_all_customers(self):
        return self.customer_table


