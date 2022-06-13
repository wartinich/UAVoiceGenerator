from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.http import HttpResponse


class SignUpPageView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'auth/sign_up.html'


class LoginPageView(View):
    """Login Page View"""
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get(self, request):
        context = {
            'form': self.form_class(),
            'message': ''
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                print('Password error')
            else:
                password = form.cleaned_data['password1']

            user = authenticate(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect('home')


        context = {
            'form': form,
        }

        return render(request, self.template_name, context=context)

