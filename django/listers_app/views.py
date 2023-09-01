from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lister
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED

class Sign_Up(APIView):
    def post (self, request):
        username = request.data['email']
        email = request.data['email']
        name = request.data['user_name']
        password = request.data['password']
        new_lister = Lister.objects.create_user(username=username, email=email, password=password, user_name=name)
        token = Token.objects.create(user=new_lister)
        return Response({
            "lister":new_lister.email,
            "name": new_lister.user_name,
            "id": new_lister.id,
            "token": token.key,
            },
            status=HTTP_201_CREATED
            )

