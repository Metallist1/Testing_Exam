from abc import ABCMeta, abstractmethod

class Customer_Repo_Interface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def get_all_customers(self):
        raise NotImplementedError