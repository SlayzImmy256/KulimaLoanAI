from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Farmer, LoanOfficer, Admin, LoanProduct, LoanApplication, Repayment, LoanDisbursement,
    Insurance, FeedbackSystem, Notification, AuditLog, MarketData
)

# --- User Views ---
class FarmerListView(ListView):
    model = Farmer
    template_name = 'loanai/farmer_list.html'

class FarmerDetailView(DetailView):
    model = Farmer
    template_name = 'loanai/farmer_detail.html'

class FarmerCreateView(CreateView):
    model = Farmer
    fields = '__all__'
    template_name = 'loanai/farmer_form.html'
    success_url = reverse_lazy('farmer-list')

class FarmerUpdateView(UpdateView):
    model = Farmer
    fields = '__all__'
    template_name = 'loanai/farmer_form.html'
    success_url = reverse_lazy('farmer-list')

class FarmerDeleteView(DeleteView):
    model = Farmer
    template_name = 'loanai/farmer_confirm_delete.html'
    success_url = reverse_lazy('farmer-list')

class LoanOfficerListView(ListView):
    model = LoanOfficer
    template_name = 'loanai/loanofficer_list.html'

class LoanOfficerDetailView(DetailView):
    model = LoanOfficer
    template_name = 'loanai/loanofficer_detail.html'

class LoanOfficerCreateView(CreateView):
    model = LoanOfficer
    fields = '__all__'
    template_name = 'loanai/loanofficer_form.html'
    success_url = reverse_lazy('loanofficer-list')

class LoanOfficerUpdateView(UpdateView):
    model = LoanOfficer
    fields = '__all__'
    template_name = 'loanai/loanofficer_form.html'
    success_url = reverse_lazy('loanofficer-list')

class LoanOfficerDeleteView(DeleteView):
    model = LoanOfficer
    template_name = 'loanai/loanofficer_confirm_delete.html'
    success_url = reverse_lazy('loanofficer-list')

class AdminListView(ListView):
    model = Admin
    template_name = 'loanai/admin_list.html'

class AdminDetailView(DetailView):
    model = Admin
    template_name = 'loanai/admin_detail.html'

class AdminCreateView(CreateView):
    model = Admin
    fields = '__all__'
    template_name = 'loanai/admin_form.html'
    success_url = reverse_lazy('admin-list')

class AdminUpdateView(UpdateView):
    model = Admin
    fields = '__all__'
    template_name = 'loanai/admin_form.html'
    success_url = reverse_lazy('admin-list')

class AdminDeleteView(DeleteView):
    model = Admin
    template_name = 'loanai/admin_confirm_delete.html'
    success_url = reverse_lazy('admin-list')

# --- LoanProduct Views ---
class LoanProductListView(ListView):
    model = LoanProduct
    template_name = 'loanai/loanproduct_list.html'

class LoanProductDetailView(DetailView):
    model = LoanProduct
    template_name = 'loanai/loanproduct_detail.html'

class LoanProductCreateView(CreateView):
    model = LoanProduct
    fields = '__all__'
    template_name = 'loanai/loanproduct_form.html'
    success_url = reverse_lazy('loanproduct-list')

class LoanProductUpdateView(UpdateView):
    model = LoanProduct
    fields = '__all__'
    template_name = 'loanai/loanproduct_form.html'
    success_url = reverse_lazy('loanproduct-list')

class LoanProductDeleteView(DeleteView):
    model = LoanProduct
    template_name = 'loanai/loanproduct_confirm_delete.html'
    success_url = reverse_lazy('loanproduct-list')

# --- LoanApplication Views ---
class LoanApplicationListView(ListView):
    model = LoanApplication
    template_name = 'loanai/loanapplication_list.html'

class LoanApplicationDetailView(DetailView):
    model = LoanApplication
    template_name = 'loanai/loanapplication_detail.html'

class LoanApplicationCreateView(CreateView):
    model = LoanApplication
    fields = '__all__'
    template_name = 'loanai/loanapplication_form.html'
    success_url = reverse_lazy('loanapplication-list')

class LoanApplicationUpdateView(UpdateView):
    model = LoanApplication
    fields = '__all__'
    template_name = 'loanai/loanapplication_form.html'
    success_url = reverse_lazy('loanapplication-list')

class LoanApplicationDeleteView(DeleteView):
    model = LoanApplication
    template_name = 'loanai/loanapplication_confirm_delete.html'
    success_url = reverse_lazy('loanapplication-list')

# --- Repayment Views ---
class RepaymentListView(ListView):
    model = Repayment
    template_name = 'loanai/repayment_list.html'

class RepaymentDetailView(DetailView):
    model = Repayment
    template_name = 'loanai/repayment_detail.html'

class RepaymentCreateView(CreateView):
    model = Repayment
    fields = '__all__'
    template_name = 'loanai/repayment_form.html'
    success_url = reverse_lazy('repayment-list')

class RepaymentUpdateView(UpdateView):
    model = Repayment
    fields = '__all__'
    template_name = 'loanai/repayment_form.html'
    success_url = reverse_lazy('repayment-list')

# --- LoanDisbursement Views ---
class LoanDisbursementListView(ListView):
    model = LoanDisbursement
    template_name = 'loanai/loandisbursement_list.html'

class LoanDisbursementDetailView(DetailView):
    model = LoanDisbursement
    template_name = 'loanai/loandisbursement_detail.html'

class LoanDisbursementCreateView(CreateView):
    model = LoanDisbursement
    fields = '__all__'
    template_name = 'loanai/loandisbursement_form.html'
    success_url = reverse_lazy('loandisbursement-list')

class LoanDisbursementUpdateView(UpdateView):
    model = LoanDisbursement
    fields = '__all__'
    template_name = 'loanai/loandisbursement_form.html'
    success_url = reverse_lazy('loandisbursement-list')

# --- Insurance Views ---
class InsuranceListView(ListView):
    model = Insurance
    template_name = 'loanai/insurance_list.html'

class InsuranceDetailView(DetailView):
    model = Insurance
    template_name = 'loanai/insurance_detail.html'

class InsuranceCreateView(CreateView):
    model = Insurance
    fields = '__all__'
    template_name = 'loanai/insurance_form.html'
    success_url = reverse_lazy('insurance-list')

class InsuranceUpdateView(UpdateView):
    model = Insurance
    fields = '__all__'
    template_name = 'loanai/insurance_form.html'
    success_url = reverse_lazy('insurance-list')

# --- FeedbackSystem Views ---
class FeedbackSystemListView(ListView):
    model = FeedbackSystem
    template_name = 'loanai/feedbacksystem_list.html'

class FeedbackSystemDetailView(DetailView):
    model = FeedbackSystem
    template_name = 'loanai/feedbacksystem_detail.html'

class FeedbackSystemCreateView(CreateView):
    model = FeedbackSystem
    fields = '__all__'
    template_name = 'loanai/feedbacksystem_form.html'
    success_url = reverse_lazy('feedbacksystem-list')

# --- Notification Views ---
class NotificationListView(ListView):
    model = Notification
    template_name = 'loanai/notification_list.html'

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'loanai/notification_detail.html'

# --- AuditLog Views ---
class AuditLogListView(ListView):
    model = AuditLog
    template_name = 'loanai/auditlog_list.html'

class AuditLogDetailView(DetailView):
    model = AuditLog
    template_name = 'loanai/auditlog_detail.html'

# --- MarketData Views ---
class MarketDataListView(ListView):
    model = MarketData
    template_name = 'loanai/marketdata_list.html'

class MarketDataDetailView(DetailView):
    model = MarketData
    template_name = 'loanai/marketdata_detail.html'
