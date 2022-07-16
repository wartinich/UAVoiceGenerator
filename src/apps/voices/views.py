from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from apps.voices.forms import CreateRecord
from apps.voices.tasks import generate_voice
from apps.voices.models import RecordHistory


class WelcomePage(View):
    def get(self, request):
        return render(request, 'home/index.html')


class VoiceGeneratorPage(LoginRequiredMixin, View):
    form_class = CreateRecord
    template_name = 'record/voice_generator.html'

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            record_text = form.cleaned_data.get('record_text')
            generate_voice(user=self.request.user, text=record_text)
            return redirect('history')

        context = {
            'form': self.form_class
        }

        return render(request, self.template_name, context=context)


class VoiceHistoryPage(LoginRequiredMixin, View):
    template_name = 'record/record_history.html'

    def get(self, request):
        context = {
            'records': RecordHistory.objects.select_related('record', 'user').filter(user=self.request.user)
        }

        return render(request, self.template_name, context)

