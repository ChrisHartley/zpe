from django.db import models


class ProcessManager(models.Manager):
    def create_process(self, title):
        process = self.create(title=title)
        # do something with the book
        return process

class Process(models.Model):
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    exit_code = models.CharField()
    records_returned = models.IntegerField()

    argument_start_date = models.DateField(blank=True, null=True)
    argument_end_date = models.DateField(blank=True, null=True)


    objects = ProcessManager()
