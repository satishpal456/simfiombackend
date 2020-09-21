import random
import string

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..serializers import UserSerializer
from ..models import User
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


class LoginViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data["username"])
            if user is not None:
                credentials = {"username": user.username, "password": request.data["password"]}
                user = authenticate(**credentials)
                if user:
                    token, created = Token.objects.get_or_create(user=user)
                    user_data = UserSerializer(user)
                    return Response({
                        "status": 200,
                        "message": "User Logged in successfully",
                        'token': token.key,
                        'data': user_data.data,
                    })
                else:
                    raise ValueError("Password is wrong")
        except User.DoesNotExist as e:
            raise ValueError("User does not exists")

