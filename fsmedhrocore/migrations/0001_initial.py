# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 02:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dozent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=30, null=True)),
                ('vorname', models.CharField(max_length=30, null=True)),
                ('nachname', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Dozent',
                'verbose_name_plural': 'Dozenten',
            },
        ),
        migrations.CreateModel(
            name='FachschaftUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'StudentIn',
                'verbose_name_plural': 'StudentInnen',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('endung', models.CharField(max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'Gender/Geschlecht',
                'verbose_name_plural': 'Gender/Geschlechter',
            },
        ),
        migrations.CreateModel(
            name='Studienabschnitt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('sortierung', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Studienabschnitt/Semester',
                'verbose_name_plural': 'Studienabschnitte/Semester',
                'ordering': ['sortierung'],
            },
        ),
        migrations.CreateModel(
            name='Studiengang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('studienabschnitt', models.ManyToManyField(blank=True, related_name='studiengang', to='fsmedhrocore.Studienabschnitt')),
            ],
            options={
                'verbose_name': 'Studiengang',
                'verbose_name_plural': 'Studiengänge',
            },
        ),
        migrations.AddField(
            model_name='fachschaftuser',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fsmedhrocore.Gender'),
        ),
        migrations.AddField(
            model_name='fachschaftuser',
            name='studienabschnitt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fsmedhrocore.Studienabschnitt'),
        ),
        migrations.AddField(
            model_name='fachschaftuser',
            name='studiengang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fsmedhrocore.Studiengang'),
        ),
        migrations.AddField(
            model_name='fachschaftuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dozent',
            name='studienabschnitt',
            field=models.ManyToManyField(to='fsmedhrocore.Studienabschnitt'),
        ),
        migrations.AddField(
            model_name='dozent',
            name='studiengang',
            field=models.ManyToManyField(to='fsmedhrocore.Studiengang'),
        ),
    ]