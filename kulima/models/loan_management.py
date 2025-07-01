from typing import Dict, Any
from .user import Farmer

class LoanProduct:
    def __init__(self, product_id: str, interest_rate: float, max_amount: float, repayment_terms: str):
        self.product_id = product_id
        self.interest_rate = interest_rate
        self.max_amount = max_amount
        self.repayment_terms = repayment_terms

    def update_terms(self, new_terms: Dict[str, Any]):
        pass

    def check_eligibility(self, farmer: Farmer):
        pass

class LoanDisbursement:
    def __init__(self, disbursement_id: str, loan_id: str, bank_transaction_id: str, status: str):
        self.disbursement_id = disbursement_id
        self.loan_id = loan_id
        self.bank_transaction_id = bank_transaction_id
        self.status = status

    def initiate_disbursement(self):
        pass

    def confirm_receipt(self):
        pass 