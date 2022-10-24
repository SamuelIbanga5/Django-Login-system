from django.db import models

class PasswordResetModel(models.Model):
    email = models.EmailField(max_length=100)
