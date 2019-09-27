import boto3
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.conf import settings
from .models import FundooNotes
from .serializers import NoteSerializer


class NoteApi(APIView):
    def get(self, request, pk):
        try:
            noted = FundooNotes.objects.get(pk=pk)
            if not noted:
                raise ValueError
            if NoteSerializer().create(noted):
                return HttpResponse('noted')
        except Exception as e:
            return HttpResponse('no such notes', e)
