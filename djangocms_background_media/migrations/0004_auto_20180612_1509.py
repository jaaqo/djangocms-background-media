# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 12:09
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_background_media', '0003_auto_20180611_1242'),
    ]

    operations = [
        migrations.RunSQL('DELETE FROM djangocm_background_media_backgroundmedia;'),
        migrations.AlterField(
            model_name='backgroundmedia',
            name='video_mp4',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_mp4', to='filer.File', verbose_name='Video mp4'),
        ),
        migrations.AlterField(
            model_name='backgroundmedia',
            name='video_ogv',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_ogv', to='filer.File', verbose_name='Video ogv'),
        ),
        migrations.AlterField(
            model_name='backgroundmedia',
            name='video_webm',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_webm', to='filer.File', verbose_name='Video webm'),
        ),
    ]