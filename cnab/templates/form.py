from django.db import models
from django import forms

class File(models.Model):
    file = models.FileField(max_length=100)


class FileForm(forms.Form):
    file = forms.FileField()