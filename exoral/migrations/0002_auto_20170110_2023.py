# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exoral', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frage',
            options={'verbose_name': 'Frage', 'verbose_name_plural': 'Fragen'},
        ),
        migrations.AlterModelOptions(
            name='kommentar',
            options={'verbose_name': 'Kommentar', 'verbose_name_plural': 'Kommentare'},
        ),
        migrations.AlterModelOptions(
            name='meldung',
            options={'verbose_name': 'Meldung', 'verbose_name_plural': 'Meldungen'},
        ),
        migrations.AlterModelOptions(
            name='pruefer',
            options={'verbose_name': 'PrüferIn', 'verbose_name_plural': 'PrüferInnen'},
        ),
        migrations.AlterModelOptions(
            name='testat',
            options={'verbose_name': 'mündl. Testat', 'verbose_name_plural': 'mündl. Testate'},
        ),
    ]
