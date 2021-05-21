from django.db import models
from datetime import datetime, date
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField(default=date.today)
    description=models.TextField(max_length=250)
    def __str__(self):
        return self.title