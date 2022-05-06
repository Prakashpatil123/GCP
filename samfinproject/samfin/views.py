from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Happy(APIView):
    def get(self,request):
        abc = request.query_params.get('data','no data')
        msg ={'info':abc}
        return Response(abc)