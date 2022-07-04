from django.urls import path
from voices.views import HomePage, VoiceGeneratorPage, VoiceHistoryPage


urlpatterns = [
    path('', WelcomePage.as_view(), name='home'),
    path('voice_generator/', VoiceGeneratorPage.as_view(), name='voice_generate'),
    path('history/', VoiceHistoryPage.as_view(), name='history'),
]
