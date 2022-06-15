from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import LoginUserForm, RegisterForm, UpdateUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterPageView(View):
    form_class = RegisterForm
    template_name = 'auth/sign_up.html'

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birth_date = form.cleaned_data.get('birth_date')
            avatar_image = form.cleaned_data.get('avatar_image')
            sex = form.cleaned_data.get('sex')

            user = authenticate(
                email=email,
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                avatar_image=avatar_image,
                sex=sex
            )

            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")

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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request,"Invalid form(Invalid username or password)")

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
            return redirect('profile')
        else:
            messages.error(request, "Invalid form(Invalid username or password)")

        context = {
            'form': self.form_class,
        }

        return render(request, self.template_name, context)

