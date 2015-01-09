# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('magazine_name', models.CharField(max_length=30)),
                ('subscriber_name', models.CharField(max_length=30)),
                ('subscriber_mobile_number', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('mode_of_payment', models.CharField(max_length=30)),
                ('subscription_start_date', models.DateField(default=None, null=True)),
                ('subscription_end_date', models.DateField(default=None, null=True)),
                ('subscriber_address', models.CharField(max_length=255)),
                ('subscriber_pincode', models.PositiveIntegerField()),
                ('subscriber_state', models.CharField(max_length=30)),
                ('subscription_id', models.CharField(unique=True, max_length=30)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
