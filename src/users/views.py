from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import LoginUserForm, RegisterForm, UpdateUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


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
            print('Invalid')

        context={
            'form': self.form_class
        }

        return render(request, self.template_name, context=context)


class UpdateUserView(LoginRequiredMixin, View):
    form_class = UpdateUserForm
    template_name = 'profile/profile.html'

    def get(self, request):
        context = {
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('schema-swagger-ui')
        else:
            messages.error(request, "Invalid form(Invalid username or password)")

        context = {
            'form': self.form_class,
        }

        return render(request, self.template_name, context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'profile/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')