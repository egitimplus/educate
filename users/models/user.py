from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    identity_number = models.CharField(unique=True, max_length=25)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    password_reset_token = models.CharField(max_length=255, blank=True)
    register_email_activate_token = models.CharField(max_length=255, blank=True)
    blocked_token = models.CharField(max_length=255, blank=True)
    country = models.PositiveSmallIntegerField(default=90)
    city = models.PositiveSmallIntegerField(default=34)
    captcha_count = models.PositiveSmallIntegerField(default=0)
    is_blocked = models.PositiveSmallIntegerField(default=0)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    school = models.ForeignKey('companies.School', related_name='user_school', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
        through='users.Role'
    )

    def __str__(self):
        return self.email

def jwt_get_secret_key(user_model):
    return user_model.jwt_secret
