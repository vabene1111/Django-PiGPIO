# Generated by Django 2.1.7 on 2019-04-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PiGPIO', '0008_auto_20190326_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='blockly_string',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='program',
            name='code',
            field=models.TextField(blank=True, default=''),
        ),
    ]
