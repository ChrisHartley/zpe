from django.db import models

# Create your models here.
class Process(models.Model):
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    exit_code = models.CharField()
    records_returned = models.IntegerField()
