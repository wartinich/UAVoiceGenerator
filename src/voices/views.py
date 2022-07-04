from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from voices.forms import CreateRecord
from voices.tasks import generate_voice
from voices.models import RecordHistory


class HomePage(View):
    def get(self, request):
        return render(request, 'home/index.html')


class VoiceGenerator(LoginRequiredMixin, View):
    form_class = CreateRecord
    template_name = 'voice_generator/voice_generator.html'

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
            return redirect("home")

        context = {
            'form': self.form_class
        }

        return render(request, self.template_name, context=context)


class VoiceHistoryPage(LoginRequiredMixin, ListView):
    model = RecordHistory
    template_name = 'record/record_history.html'

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = RecordHistory.objects.select_related('record', 'user').filter(user=self.request.user)
        return context

