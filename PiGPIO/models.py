from django.db import models


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128, default="")
    description = models.CharField(max_length=1024, default="")


class ProgramStep(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    type = models.CharField(max_length=32)
    successor_true = models.ForeignKey('self', on_delete=models.CASCADE, related_name='step_successor_true', null=True)
    successor_false = models.ForeignKey('self', on_delete=models.CASCADE, related_name='step_successor_false', null=True)
    pin = models.IntegerField(null=True)
    data = models.CharField(max_length=128, default="")
