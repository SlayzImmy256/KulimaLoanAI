from django.db import models

# Concrete base user
class Client(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Farmer(Client):
    # Add farmer-specific fields if needed
    pass

class LoanOfficer(Client):
    bank_affiliation = models.CharField(max_length=100)

class Admin(Client):
    access_level = models.CharField(max_length=50)

class LoanProduct(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    interest_rate = models.FloatField()
    max_amount = models.FloatField()
    repayment_terms = models.TextField()

class LoanApplication(models.Model):
    application_id = models.CharField(max_length=100, unique=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Repayment(models.Model):
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    amount = models.FloatField()
    paid = models.BooleanField(default=False)  # type: ignore
    paid_at = models.DateTimeField(null=True, blank=True)

class LoanDisbursement(models.Model):
    disbursement_id = models.CharField(max_length=100, unique=True)
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    bank_transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    disbursed_at = models.DateTimeField(auto_now_add=True)

class Insurance(models.Model):
    policy_id = models.CharField(max_length=100, unique=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    coverage_details = models.TextField()
    premium = models.FloatField()
    status = models.CharField(max_length=50)

class FeedbackSystem(models.Model):
    feedback_id = models.CharField(max_length=100, unique=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    message = models.TextField()
    recipient = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    sent_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()

class MarketData(models.Model):
    region = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()
