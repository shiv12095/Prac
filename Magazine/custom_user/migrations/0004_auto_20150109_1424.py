# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_authuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='gender',
            field=models.CharField(max_length=1),
            preserve_default=True,
        ),
    ]
