from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny
from rest_framework.response import Response
from ..models import *
from ..serializers import UserSerializer
from django.db.models import Q


class RelationViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        print()
        return User.objects.filter(id=self.request.query_params["user"])

    # def get_serializer_class(self):
    #     if self.request.method in SAFE_METHODS:
    #         return FollowingGetSerializer
    #     return FollowingSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     print(self.request.data)
    #     if self.request.method == "POST" and "PUT":
    #         context.update({"user": self.request.user, "following_user": self.request.data["following_user"]})
    #     else:
    #         context.update({"user": self.request.user})
    #     return context

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response = {
            "status": "success",
            "message": "Relation created successfully",
            "data": response.data,
            "status_code": 200,
        }
        return JsonResponse(response)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {
            "status": "success",
            "message": "Relation list",
            "data": response.data,
            "status_code": 200,
        }
        return JsonResponse(response)

    def partial_update(self, request, *args, **kwargs):
        partial_response = super().partial_update(request, *args, **kwargs)
        return Response(partial_response.data)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response = {
            "status": "success",
            "message": "Relation updated successfully",
            "data": response.data,
            "status_code": 200,
        }
        return Response(response)