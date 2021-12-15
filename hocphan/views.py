from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Majors
from .models import Docs
from .serializers import GetAllUserSerializer


# Create your views here.
class GetAllMajor(APIView):
    def get(self, request):
        list_user = Majors.objects.all()
        mydata = GetAllUserSerializer(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

# Create your views here.
# class GetAllDoc(APIView):
#     def get(self, request):
#         list_user = Majors.objects.all()
#         mydata = GetAllUserSerializer(list_user, many=True)
#         return Response(data=mydata.data, status=status.HTTP_200_OK)