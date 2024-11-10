from django.db import models

class Dictionary(models.Model):
    russian = models.CharField('Русские', max_length=128)
    uzbek = models.CharField('Узбекские', max_length=128)