# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='date_joined',
            field=models.DateField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authuser',
            name='date_of_birth',
            field=models.DateField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authuser',
            name='first_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authuser',
            name='last_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
