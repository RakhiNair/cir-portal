# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20160609_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Branch', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_course',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Current Course', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=32, null=True, verbose_name='First Name', blank=True),
        ),
    ]
