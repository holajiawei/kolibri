# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-01 19:50
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20170607_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentnode',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Language'),
        ),
        migrations.AddField(
            model_name='language',
            name='lang_direction',
            field=models.CharField(choices=[('ltr', 'Left to Right'), ('rtl', 'Right to Left')], default='ltr', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='lang_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.CharField(max_length=14, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='lang_subcode',
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
    ]