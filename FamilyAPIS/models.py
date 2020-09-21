from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(AbstractUser):
    class Meta:
        db_table = "user__userdata"
        ordering = ("id",)

    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=240, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    relatives = models.ManyToManyField('FamilyMember', related_name="family_member", blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class FamilyMember(models.Model):
    user = models.ForeignKey(User, related_name="current_user", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=240, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    relation = models.CharField(max_length=240, null=True, blank=True)
