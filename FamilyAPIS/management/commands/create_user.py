from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.db import migrations


def create_user():
    from FamilyAPIS.models import User

    user = User.objects.create_user(
        username="satishpal",
        email="satish@yopmail.com",
        first_name="satish",
        last_name="pal",
        is_active=True,
        is_superuser=False,
        is_staff=False,
    )
    user.set_password("satish123")
    user.save()
    print(f"User created with  password")


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_user()
