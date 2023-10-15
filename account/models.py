import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .userManger import UserManager
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField


# Create your models here.


class Passion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    passion = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='passion/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.passion)


class IdealMatch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    ideal_match = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='idealMatch/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ideal_match)


class Gender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    gender = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='gender/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender


class MaritalStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    marital_status = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='martialStatus/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marital_status


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    education = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='education/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.education


class BodyType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    body = models.CharField(max_length=40, blank=True, unique=True)
    image = models.ImageField(upload_to='education/')
    color = ColorField(format='hexa')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Up to 15 digits allowed.")
    email = models.EmailField(_("email address"), unique=True, max_length=200)
    username = None
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    root_uuid = models.UUIDField(blank=True, null=True)
    root_user = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    is_root_user = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")
    is_team_member = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")
    is_premium = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")
    is_verified = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")
    is_private = models.BooleanField(default=False, blank=True)

    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    image = models.ImageField(upload_to="profile/image/", blank=True, null=True)
    website_link = models.CharField(max_length=500, blank=True, null=True)

    about = models.TextField(default=None, blank=True, null=True)
    is_about = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    birth_date = models.DateField(default='1999-12-15', blank=True)
    is_birth_date = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    education = models.ManyToManyField(Education, blank=True)
    is_education = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    street_address = models.CharField(max_length=500, blank=True, null=True)
    county = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    location = models.PointField(srid=4326, blank=True, null=True)
    is_location = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    passion = models.ManyToManyField(Passion, blank=True)
    is_passion = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    ideal_match = models.ManyToManyField(IdealMatch, blank=True)
    is_ideal_match = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='users_with_gender')
    is_gender = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    marital_status = models.ManyToManyField(MaritalStatus, blank=True)
    is_marital_status = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    interest_in = models.ForeignKey('Gender', on_delete=models.SET_NULL, blank=True, related_name='users_interested_in', null=True)
    is_interest = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    height = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    is_height = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    body_type = models.ManyToManyField(BodyType, blank=True)
    is_body_type = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class UserMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="userMedia/image/", default=None, blank=True,null=True)
    video = models.FileField(upload_to="userMedia/video/", default=None, blank=True, null=True)
    is_private = models.BooleanField(default=False, blank=True, help_text="Enable or Disable")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
