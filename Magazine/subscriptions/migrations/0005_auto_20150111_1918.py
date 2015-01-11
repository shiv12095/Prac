# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_magazinesubscription_cancelled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazinesubscription',
            name='cancelled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
