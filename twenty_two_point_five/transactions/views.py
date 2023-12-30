
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT,WITHDRAWAL
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from accounts.models import Bank
from datetime import datetime
from django.db.models import Sum

from transactions.forms import (
    DepositForm,
    WithdrawForm,
)
from transactions.models import Transaction

def send_transaction_email(user,amount,subject,template):
        message = render_to_string(template,{
            'user':user,
            'amount':amount,
        })
        send_email=EmailMultiAlternatives(subject,'',to=[user.email])
        send_email.attach_alternative(message,"text/html")
        send_email.send()


class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account':self.request.user.account,
        })
        return kwargs

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        return context
    
class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'
 
    def get_initial(self):
        initial = {'transaction_type':DEPOSIT}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"{amount}$ was deposited to your account successfully")

        # send_transaction_email(self.request.user,amount,"Deposite Message","transactions/deposite_email.html")

        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'
    
    context_object_name = 'bank_model_instance'

    def get_initial(self):
        initial = {'transaction_type':WITHDRAWAL}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        try:
            bank_model_instance=Bank.objects.get(id=1)
        except Bank.DoesNotExist:
            messages.error(self.request, "Error: Bank instance not found.")
            return self.form_invalid(form)
    
        if bank_model_instance.is_bankrupt:
            messages.error(self.request, "Error: Bank is bankrupt")
            return self.form_invalid(form)
        
        if amount <= account.balance:
            account.balance -= amount
            account.save()
            messages.success(self.request,f"successfully withdrawn {amount}$ from your account")

            # send_transaction_email(self.request.user,amount,"Withdraw Message","transactions/withdrawal_email.html")

            return super().form_valid(form)
        else:
            messages.error(self.request, "Error: Insufficient balance for the withdrawal.")
            return self.form_invalid(form)
    

