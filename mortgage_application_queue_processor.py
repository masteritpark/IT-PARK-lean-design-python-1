from exceptions import WrongDataException
from exceptions import NotEligibleForMortgageException


class MortgageApplicationQueueProcessor:
    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def process_request(self, customer_id, amount_requested):
        customer = self.customer_repository.get_customer(customer_id)

        if customer is None:
            raise WrongDataException('Customer not found!')

        if not customer.is_eligible_for_mortgage(amount_requested):
            raise NotEligibleForMortgageException

        customer.update_balance(amount_requested)