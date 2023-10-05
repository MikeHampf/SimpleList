from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lister
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT

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
    
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        lister = authenticate(username=email, password=password)
        if lister:
            token, created = Token.objects.get_or_create(user=lister)
            return Response(
                {
                    "token": token.key,
                    "lister": lister.user_name,
                    "email": lister.email,
                    "id": lister.id,
                },
                status=HTTP_200_OK
            )
        
class Logout(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response("YOU'VE BEEN LOGGED OUT", status=HTTP_204_NO_CONTENT)
    
class Unsubscribe(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        return Response("YOU'VE BEEN DELETED", status=HTTP_204_NO_CONTENT)
    
class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
                    "email": request.user.email,
                    "user_name": request.user.user_name,
                    "id": request.user.id,
                    "date_joined": request.user.date_joined
                         },
                         status=HTTP_200_OK)

