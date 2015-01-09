# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20150109_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazinesubscription',
            name='subscriber_mobile_number',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
