class Customer:
    def __init__(self, _id, first_name, last_name,
                 balance, bad_credit_history_count):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.bad_credit_history_count = bad_credit_history_count

    def update_balance(self, amount):
        self.balance = self.balance + amount
