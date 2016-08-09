# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_administrateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_prod', models.CharField(max_length=200)),
                ('desg_prod', models.CharField(max_length=200)),
                ('image_prod', models.CharField(max_length=200)),
            ],
        ),
    ]