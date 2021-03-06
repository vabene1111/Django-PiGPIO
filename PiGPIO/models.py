from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128, default='')
    description = models.CharField(_('Description'), max_length=1024, default='', blank=True)
    blockly_string = models.TextField(_('Blockly XML'), blank=True, default='')
    code = models.TextField(blank=True, default='')
    running = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Log(models.Model):
    INFO = 'INFO'
    ERROR = 'ERROR'
    LOG = 'LOG'
    DEBUG = 'DEBUG'

    data = models.CharField(max_length=256)
    tag = models.CharField(max_length=32, choices=((INFO, _('INFO')), (ERROR, _('ERROR')), (LOG, _('LOG')), (DEBUG, _('DEBUG'))), default=INFO)
    created_at = models.DateTimeField(auto_now_add=True)


class Dashboard(models.Model):
    name = models.CharField(max_length=128)
    text = models.CharField(max_length=32, default='', blank=True)
    row = models.CharField(_('Row'), max_length=1, choices=(('1', '1'), ('2', '2'), ('3', '3')), default=1)
    col = models.CharField(_('Column'), max_length=1, choices=(('1', '1'), ('2', '2'), ('3', '3')), default=1)
    background_color = models.CharField(_('Background color'), max_length=8, default='#247896')
    font_color = models.CharField(_('Text Color'), max_length=8, default='#ffffff')
    icon = models.CharField(max_length=32, default='', blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
