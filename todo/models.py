from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=100, blank=True, default="")
    note = models.TextField(max_length=1000, blank=True, default="")
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
