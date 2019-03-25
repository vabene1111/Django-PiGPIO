from django.db import models


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128, default="")
    description = models.CharField(max_length=1024, default="")
    running = models.BooleanField(default=False)
    logging = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProgramStep(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    num = models.IntegerField()
    type = models.CharField(max_length=32)
    successor_true = models.IntegerField(null=True)
    successor_false = models.IntegerField(null=True)
    pin = models.IntegerField(null=True)
    data = models.CharField(max_length=128, default="", null=True)

    def __str__(self):
        return 'Program: ' + str(self.program) + ' Num: ' + str(self.num) + ' Type: ' + self.type + ' Pin: ' + str(self.pin)


# Create your models here.
class ProgramLog(models.Model):
    step = models.ForeignKey(ProgramStep, on_delete=models.CASCADE, null=True)
    info = models.CharField(max_length=256, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at) + ' - ' + str(self.step)
