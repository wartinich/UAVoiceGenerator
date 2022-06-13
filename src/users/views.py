from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import LoginUserForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


class SignUpPageView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'auth/sign_up.html'


class LoginPageView(View):
    """Login Page View"""
    template_name = 'auth/login.html'
    form_class = LoginUserForm

    def get(self, request):
        context = {
            'form': self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                redirect('admin')
            else:
                return HttpResponse('Invalid login')

        else:
            return HttpResponse('Invalid form')

        context = {
            'form': form,
        }

        return render(request, self.template_name, context=context)

