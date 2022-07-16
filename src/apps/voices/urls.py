from django.urls import path
from apps.voices.views import WelcomePage, VoiceGeneratorPage, VoiceHistoryPage


urlpatterns = [
    path('', WelcomePage.as_view(), name='welcome'),
    path('voice_generator/', VoiceGeneratorPage.as_view(), name='voice_generate'),
    path('history/', VoiceHistoryPage.as_view(), name='history'),
]
