from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import serializers
from .models import *


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = FamilyMember
        fields = (
            "id", "name", "relation", "created_at", "user"
        )
        read_only_fields = ("id",)


class UserSerializer(serializers.ModelSerializer):
    relatives = FamilySerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id", "username", "first_name", "last_name", "email",
            "phone_number", "address", "relatives",
            "date_of_birth"
        )
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id",)



