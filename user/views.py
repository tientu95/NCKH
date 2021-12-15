from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import GetAllUserSerializer, UserSerializer


# Create your views here.
class GetAllUser(APIView):
    def get(self, request):
        list_user = User.objects.all()
        mydata = GetAllUserSerializer(list_user, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
    def post(self, request):
        mydata=UserSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Loi', status=status.HTTP_400_BAD_REQUEST)
        user_id = mydata.data('user_id')
        user_mail = mydata.data('user_mail')
        user_pass = mydata.data('user_pass')
        user_name = mydata.data('user_name')
        user_phone = mydata.data('user_phone')
        decent_id = mydata.data('decent')
        cs = User.objects.create(user_id=user_id, user_mail=user_mail, user_pass=user_pass, user_name=user_name, user_phone=user_phone, decent=decent_id)
        return Response(data=cs.user_id, status=status.HTTP_200_OK)