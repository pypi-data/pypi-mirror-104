# Generated by Django 2.2.18 on 2021-03-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vstutils_api', '0002_two_factor'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='recoverycode',
            index=models.Index(fields=['id', 'key', 'tfa'], name='%(app_label)s_recov_fullidx'),
        ),
        migrations.AddIndex(
            model_name='twofactor',
            index=models.Index(fields=['user', 'secret'], name='%(app_label)s_tfa_fullidx'),
        ),
    ]
