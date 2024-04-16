from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details=models.TextField()
    date = models.DateTimeField(default=timezone.now)


def __str__(self):
    # The __str__() function controls what should be returned when the class object is represented as a string.
    return self.title