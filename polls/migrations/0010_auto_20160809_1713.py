# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20160809_1637'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrateur',
        ),
        migrations.DeleteModel(
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_clt',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='ref_prod',
        ),
        migrations.RemoveField(
            model_name='facture',
            name='id_clt',
        ),
        migrations.RemoveField(
            model_name='facture',
            name='id_cmde',
        ),
        migrations.RemoveField(
            model_name='message',
            name='login_clt',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='id_clt',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='ref_prod',
        ),
        migrations.DeleteModel(
            name='Vendeur',
        ),
        migrations.AddField(
            model_name='choice',
            name='tts',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
        migrations.DeleteModel(
            name='Facture',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='panier',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
    ]