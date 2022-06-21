from django.urls import path
from voices.views import HomePage, VoiceGeneratorPage


urlpatterns = [
    path('', HomePage.as_view()),
    path('voice_generator', VoiceGeneratorPage.as_view())
]