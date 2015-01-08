# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20150108_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='gender',
            field=models.CharField(default='a', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
    ]
