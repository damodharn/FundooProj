from django.db import models
from django.contrib.auth.models import User


class FundooNotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    note = models.TextField(max_length=1025)
    reminder = models.DateTimeField()
    collaborator = models.EmailField(max_length=255)
    color = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images/")
    archive = models.BooleanField(default=False)
