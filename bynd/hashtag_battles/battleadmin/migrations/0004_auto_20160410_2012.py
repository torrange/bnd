# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleadmin', '0003_remove_battle_hashtag_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='hashtag_1',
            field=models.ManyToManyField(related_name='hashtag_1', to='battleadmin.Hashtag'),
        ),
        migrations.AddField(
            model_name='battle',
            name='hashtag_2',
            field=models.ManyToManyField(related_name='hashtag_2', to='battleadmin.Hashtag'),
        ),
    ]
