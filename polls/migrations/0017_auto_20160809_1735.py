# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20160809_1732'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrateur',
        ),
        migrations.DeleteModel(
            name='Vendeur',
        ),
    ]