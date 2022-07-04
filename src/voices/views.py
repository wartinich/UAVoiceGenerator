from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from voices.tasks import generate_voice
from django.http import HttpResponse


class HomePage(View):
    def get(self, request):
        return render(request, 'home/index.html')


class VoiceGenerator(LoginRequiredMixin, View):
    def get(self, request):
        generate_voice()
        return redirect("home")