from rest_framework import generics, viewsets
from django.shortcuts import redirect
from api.serializers import RecordHistorySerializer, VoiceGenerateSerializer
from voices.models import RecordHistory
from rest_framework.response import Response
from voices.tasks import generate_voice
from drf_yasg.utils import swagger_auto_schema


class RecordViewSet(viewsets.ViewSet):
    @swagger_auto_schema(tags=['records'])
    def list(self, request, *args, **kwargs):
        queryset = RecordHistory.objects.filter(user=self.request.user)
        serializer = RecordHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['records'])
    def create(self, request, *args, **kwargs):
        serializer = VoiceGenerateSerializer(data=request.data)
        if serializer.is_valid():
            record_text = serializer.data.get('text')
            generate_voice(user=self.request.user, text=record_text)
            return redirect('record_history')
