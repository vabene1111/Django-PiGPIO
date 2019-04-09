from django.db import models


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128, default='')
    description = models.CharField(max_length=1024, default='', blank=True)
    blockly_string = models.TextField(blank=True, default='')
    code = models.TextField(blank=True, default='')
    running = models.BooleanField(default=False)

    def __str__(self):
        return self.name
