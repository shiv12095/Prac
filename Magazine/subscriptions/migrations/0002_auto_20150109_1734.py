# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazinesubscription',
            name='subscriber_mobile_number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
