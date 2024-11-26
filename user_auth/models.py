import uuid
from django.db import models
from django.core.validators import MinValueValidator


class Users(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    user_name = models.CharField(max_length=100)
    age = models.IntegerField(
        default=18,
        validators=[
            MinValueValidator(18)
        ]
    )
    email = models.CharField(max_length=100)
    hashed_password = models.CharField(max_length=74)
