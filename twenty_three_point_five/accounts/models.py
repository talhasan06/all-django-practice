from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

class Bank(models.Model):
    is_bankrupt = models.BooleanField(default=False)

class UserBankAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date=models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)

    def __str__(self):
        return str(self.account_no)
    
    def transfer_balance(self, target_account_no, amount,request_user):
        source_account = self
        try:
            target_account = UserBankAccount.objects.get(account_no=target_account_no)
        except UserBankAccount.DoesNotExist:
            raise ValidationError("Error: Target account not found.")
            # return "Error: Target account not found."

        if self.balance < amount:
            raise ValidationError("Error: Insufficient balance for the transfer.")

        source_account.balance -= amount
        target_account.balance += amount

        source_account.save()
        target_account.save()

        # Send email to the sender
        sender_message = render_to_string('transfer_email_sender.html', {
            'sender': source_account.user,
            'receiver_account_no': target_account_no,
            'amount': amount,
        })
        sender_subject = 'Balance Transfer Confirmation'
        sender_email = EmailMultiAlternatives(sender_subject, strip_tags(sender_message), to=[source_account.user.email])
        sender_email.attach_alternative(sender_message, "text/html")
        sender_email.send()

        # Send email to the receiver
        receiver_message = render_to_string('transfer_email_receiver.html', {
            'sender_user': source_account.user,
            'receiver_user': target_account.user,
            'amount': amount,
        })
        receiver_subject = 'Received Balance'
        receiver_email = EmailMultiAlternatives(receiver_subject, strip_tags(receiver_message), to=[target_account.user.email])
        receiver_email.attach_alternative(receiver_message, "text/html")
        receiver_email.send()

        return "Success: Balance transferred successfully."
    
class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.user.email)
