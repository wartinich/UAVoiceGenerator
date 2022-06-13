from django.views.generic import View
from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.http import HttpResponse


class LoginPageView(View):
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
                message = 'Password error'
            else:
                password = form.cleaned_data['password1']

            user = authenticate(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=password,
            )
            if user is not None:
                login(request, user)
                return HttpResponse('++++==')
        message = 'Login failed!'

        context = {
            'form': form,
            'message': message
        }

        return render(request, self.template_name, context=context)

