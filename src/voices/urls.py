from django.urls import path
from voices.views import HomePage, VoiceGenerator


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('voice_generator/', VoiceGenerator.as_view(), name='voice_generate')
]