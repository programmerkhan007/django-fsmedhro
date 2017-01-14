# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 02:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fsmedhrocore', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExoralUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pruefer',
            fields=[
                ('dozent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fsmedhrocore.Dozent')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'PrüferIn',
                'verbose_name_plural': 'PrüferInnen',
            },
            bases=('fsmedhrocore.dozent',),
        ),
        migrations.CreateModel(
            name='Testat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('pruefer', models.ManyToManyField(to='exoral.Pruefer')),
                ('studienabschnitt', models.ManyToManyField(to='fsmedhrocore.Studienabschnitt')),
                ('studiengang', models.ManyToManyField(to='fsmedhrocore.Studiengang')),
            ],
            options={
                'verbose_name': 'mündl. Testat',
                'verbose_name_plural': 'mündl. Testate',
            },
        ),
        migrations.CreateModel(
            name='Textbeitrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(blank=True)),
                ('text', models.TextField()),
                ('sichtbar', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Frage',
            fields=[
                ('textbeitrag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exoral.Textbeitrag')),
                ('datum', models.DateField(default=datetime.datetime.today)),
                ('score', models.PositiveIntegerField(default=1)),
                ('antwort', models.TextField(blank=True, null=True)),
                ('pruefer', models.ManyToManyField(to='exoral.Pruefer')),
                ('testat', models.ManyToManyField(to='exoral.Testat')),
            ],
            options={
                'verbose_name': 'Frage',
                'verbose_name_plural': 'Fragen',
            },
            bases=('exoral.textbeitrag',),
        ),
        migrations.CreateModel(
            name='Kommentar',
            fields=[
                ('textbeitrag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exoral.Textbeitrag')),
                ('pruefer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoral.Pruefer')),
            ],
            options={
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
            },
            bases=('exoral.textbeitrag',),
        ),
        migrations.CreateModel(
            name='Meldung',
            fields=[
                ('textbeitrag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exoral.Textbeitrag')),
                ('bearbeitet', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Meldung',
                'verbose_name_plural': 'Meldungen',
            },
            bases=('exoral.textbeitrag',),
        ),
        migrations.AddField(
            model_name='textbeitrag',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='textbeitrag',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meldung',
            name='beitrag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meldungen', to='exoral.Textbeitrag'),
        ),
    ]