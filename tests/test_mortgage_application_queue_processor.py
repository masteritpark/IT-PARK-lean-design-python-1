from unittest import TestCase
from unittest import mock


from domain.customer import Customer
from exceptions import WrongDataException
from exceptions import NotEligibleForMortgageException
from mortgage_application_queue_processor import (
    MortgageApplicationQueueProcessor
)


class TestMortgageApplicationQueueProcessor(TestCase):

    def test_wrong_data_provided(self):
        customer_repository = mock.MagicMock()
        customer_repository.get_customer.return_value = None
        maqp = MortgageApplicationQueueProcessor(customer_repository)

        with self.assertRaises(WrongDataException):
            maqp.process_request(1, 2)

        customer_repository.get_customer.assert_called_once_with(1)

    def test_not_eligible_exception(self):
        customer = Customer(
            _id=1,
            first_name='first',
            last_name='last',
            balance=0,
            bad_credit_history_count=10
        )
        customer_repository = mock.MagicMock()
        customer_repository.get_customer.return_value = customer
        maqp = MortgageApplicationQueueProcessor(customer_repository)

        with self.assertRaises(NotEligibleForMortgageException):
            maqp.process_request(1, 2)

        customer_repository.get_customer.assert_called_once_with(1)

    def test_mortgage_approved(self):
        balance = 1000
        requested_amount = 500
        expected_result = balance + requested_amount
        customer = Customer(
            _id=1,
            first_name='first',
            last_name='last',
            balance=balance,
            bad_credit_history_count=0
        )
        customer_repository = mock.MagicMock()
        customer_repository.get_customer.return_value = customer
        maqp = MortgageApplicationQueueProcessor(customer_repository)

        maqp.process_request(1, requested_amount)

        self.assertEqual(expected_result, customer.balance)