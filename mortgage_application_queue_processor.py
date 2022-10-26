from exceptions import WrongDataException
from exceptions import NotEligibleForMortgageException


class MortgageApplicationQueueProcessor:
    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def process_request(self, customer_id, amount_requested):
        customer = self.customer_repository.get_customer(customer_id)

        if customer is None:
            raise WrongDataException('Customer not found!')

        if not self.is_eligible_for_mortgage(customer, amount_requested):
            raise NotEligibleForMortgageException

        customer.update_balance(amount_requested)

    def is_eligible_for_mortgage(self, customer, amount_requested):
        is_eligible = False
        if customer.bad_credit_history_count == 0 and customer.balance > 0:
            is_eligible = customer.balance * 2 >= amount_requested

        return is_eligible
