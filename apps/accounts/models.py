from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    ROLES=(("0", "Admin"), ("1", "Journalist"), ("2", "Guest"))
    role = models.CharField(max_length=1, choices=ROLES)
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= "username", "role"

class UserProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address= models.CharField(max_length=50, blank=True)
    dob= models.DateField(blank=True)
