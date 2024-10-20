from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

