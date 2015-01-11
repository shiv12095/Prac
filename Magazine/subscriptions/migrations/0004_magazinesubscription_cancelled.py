# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20150109_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazinesubscription',
            name='cancelled',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
