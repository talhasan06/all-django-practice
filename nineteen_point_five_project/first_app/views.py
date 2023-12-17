from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
        
    return render(request,'register.html',{'form':register_form,'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        messages.success(self.request,'musician added successfully')
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Musician'
        return context
    
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        messages.success(self.request,'Album created successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Album'
        return context

class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class DeleteMusicianView(DeleteView):
    model = models.Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg='id'