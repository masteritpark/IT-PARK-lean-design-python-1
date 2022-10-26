from abc import ABC
from abc import abstractmethod


class CustomerRepository(ABC):

    @abstractmethod
    def get_customer(self, _id):
        raise NotImplementedError
