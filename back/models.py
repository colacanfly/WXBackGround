from django.db import models

# Create your models here.
from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=20)
