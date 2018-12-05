# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-29 07:59
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models

import mayan.apps.documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0042_auto_20180403_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentversion',
            name='encoding',
            field=models.CharField(blank=True, editable=False, max_length=64, null=True, verbose_name='Encoding'),
        ),
        migrations.AlterField(
            model_name='documentversion',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/rosarior/development/mayan-edms/mayan/media/document_storage'), upload_to=mayan.apps.documents.models.UUID_FUNCTION, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='documentversion',
            name='mimetype',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='MIME type'),
        ),
    ]
