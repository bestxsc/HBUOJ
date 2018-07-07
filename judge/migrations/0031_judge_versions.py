# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 00:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0030_remove_contest_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuntimeVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='', max_length=64, verbose_name='runtime name')),
                ('version', models.CharField(blank=True, help_text='', max_length=64, verbose_name='runtime version')),
                ('priority', models.IntegerField(default=0, help_text='', verbose_name='order in which to display this runtime')),
                ('judge', models.ForeignKey(help_text='', on_delete=django.db.models.deletion.CASCADE, to='judge.Judge', verbose_name='judge on which this runtime exists')),
            ],
        ),
        migrations.AlterField(
            model_name='contesttag',
            name='name',
            field=models.CharField(help_text='', max_length=20, unique=True, validators=[django.core.validators.RegexValidator(b'^[a-z-]+$', message='Lowercase letters and hyphens only.')], verbose_name='tag name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='ace',
            field=models.CharField(help_text='Language ID for Ace.js editor highlighting, appended to "mode-" to determine the Ace JavaScript file to use, e.g., "python".', max_length=20, verbose_name='ace mode name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='common_name',
            field=models.CharField(help_text='Common name for the language. For example, the common name for C++03, C++11, and C++14 would be "C++"', max_length=10, verbose_name='common name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='description',
            field=models.TextField(blank=True, help_text='Use field this to inform users of quirks with your environment, additional restrictions, etc.', verbose_name='language description'),
        ),
        migrations.AlterField(
            model_name='language',
            name='extension',
            field=models.CharField(help_text='The extension of source files, e.g., "py" or "cpp".', max_length=10, verbose_name='extension'),
        ),
        migrations.AlterField(
            model_name='language',
            name='info',
            field=models.CharField(blank=True, help_text="Do not set this unless you know what you're doing! It will override the usually more specific, judge-provided runtime info!", max_length=50, verbose_name='runtime info override'),
        ),
        migrations.AlterField(
            model_name='language',
            name='key',
            field=models.CharField(help_text='The identifier for this language; the same as its executor id for judges.', max_length=6, unique=True, verbose_name='short identifier'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Longer name for the language, e.g. "Python 2" or "C++11".', max_length=20, verbose_name='long name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='pygments',
            field=models.CharField(help_text='Language ID for Pygments highlighting in source windows.', max_length=20, verbose_name='pygments name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='short_name',
            field=models.CharField(blank=True, help_text='More readable, but short, name to display publicly; e.g. "PY2" or "C++11". If left blank, it will default to the short identifier.', max_length=10, null=True, verbose_name='short name'),
        ),
        migrations.AddField(
            model_name='runtimeversion',
            name='language',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.CASCADE, to='judge.Language', verbose_name='language to which this runtime belongs'),
        ),
    ]