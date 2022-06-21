from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class HomePage(View):
    def get(self, request):
        return render(request, 'home/index.html')


class VoiceGeneratorPage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'voice_generator/voice_generator.html')