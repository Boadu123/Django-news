from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import CreateView, FormView

from .forms import CustomUserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.template import RequestContext
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

