from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .forms import TransferBalanceForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

def send_transaction_email(user,username,subject,template):
        message = render_to_string(template,{
            'user':user,
            'username':username,
        })
        send_email=EmailMultiAlternatives(subject,'',to=[user.email])
        send_email.attach_alternative(message,"text/html")
        send_email.send()

class UserRegistrationFormView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(View):
     def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))

class UserBankAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
        return render(request, self.template_name, {'form': form})
    
class TransferBalanceView(View):
    template_name = 'transfer_balance.html'

    def get(self, request, *args, **kwargs):
        form = TransferBalanceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TransferBalanceForm(request.POST)

        if form.is_valid():
            target_account_no = form.cleaned_data['target_account_no']
            transfer_amount = form.cleaned_data['transfer_amount']

            source_account = request.user.account

            try:
                source_account.transfer_balance(target_account_no, transfer_amount, request.user)
                messages.success(request, "Balance transferred successfully.")

            except ValidationError as e:
                messages.error(request, str(e))

            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')  # Change 'profile' to the actual URL of your profile page

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, 'Your password was successfully updated!')
        send_transaction_email(self.request.user,username,"Password Changed","password_change_notification.html")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_invalid(form)
    