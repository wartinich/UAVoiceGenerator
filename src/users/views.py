from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import LoginUserForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# class SignUpPageView(CreateView):
#     form_class = RegisterForm
#     success_url = reverse_lazy('login')
#     template_name = 'auth/sign_up.html'


class RegisterPageView(View):
    form_class = RegisterForm
    template_name = 'auth/sign_up.html'

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.data()
            login(request, user)
            messages.success(request, "Registration successful.")
        else:
            messages.error(request, "Invalid form(Invalid username or password)")

        context = {
            'form': self.form_class
        }

        return render(request, self.template_name, context=context)


class LoginPageView(View):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get(self, request):
        context = {
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("schema-swagger-ui")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request,"Invalid form(Invalid username or password)")

        context={
            'form': self.form_class
        }

        return render(request, self.template_name, context=context)

