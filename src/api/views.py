from rest_framework import generics
from django.shortcuts import render, redirect
from api.serializers import RecordHistorySerializer, VoiceGenerateSerializer
from voices.models import RecordHistory
from rest_framework.views import APIView
from voices.tasks import generate_voice


class RecordHistoryView(generics.ListAPIView):
    serializer_class = RecordHistorySerializer

    def get_queryset(self):
        return RecordHistory.objects.filter(user=self.request.user)


class VoiceGeneratorView(APIView):
    def post(self, request):
        serializer = VoiceGenerateSerializer(data=request.data)
        if serializer.is_valid():
            record_text = serializer.data.get('text')
            generate_voice(user=self.request.user, text=record_text)
            return redirect('record_history')



