from django.db import models


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128, default="")
    description = models.CharField(max_length=1024, default="")


class ProgramStep(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    num = models.IntegerField()
    type = models.CharField(max_length=32)
    successor_true = models.IntegerField(null=True)
    successor_false = models.IntegerField(null=True)
    pin = models.IntegerField(null=True)
    data = models.CharField(max_length=128, default="", null=True)
