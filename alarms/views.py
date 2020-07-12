from django.shortcuts import render
from rest_framework.views import APIView
from .logic import CalculateCurrentStatus 
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class ConnectView(APIView):

    def get(self, request):
        status = CalculateCurrentStatus().execute()
        return Response({"status":status})
